#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scan-egress.py — 数据出境与敏感信息模式扫描器。

用途 : 扫描代码/配置文件，找出疑似的数据出境与敏感信息风险。
用法 : python scan-egress.py <路径1> [路径2 ...]
退出码: 0 = 无高危发现; 1 = 发现高危项; 2 = 参数错误

依赖 : Python 3.9+，仅标准库，无网络请求，无第三方包。
注意 : 本脚本只做模式匹配，输出为「疑似」，最终判定必须由人工完成。
       误报是设计上的取舍——漏报的代价远高于多看几条告警。
"""

import os
import re
import sys
from typing import Iterator, List, NamedTuple, Pattern

# ---------------------------------------------------------------- 扫描配置

# 需要跳过的目录（噪音大且与业务无关）
SKIP_DIRS = {
    ".git", "node_modules", "dist", "build", "out", ".next", ".nuxt",
    "coverage", "__pycache__", ".venv", "venv", ".idea", ".vscode",
    "target", ".gradle", "bin", "obj", ".cache", ".turbo",
}

# 跳过的二进制/大文件后缀
SKIP_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".svg", ".webp",
    ".woff", ".woff2", ".ttf", ".eot", ".otf",
    ".pdf", ".zip", ".tar", ".gz", ".rar", ".7z", ".jar", ".war",
    ".mp4", ".avi", ".mov", ".mp3", ".wav",
    ".so", ".dll", ".exe", ".dylib", ".class", ".pyc",
    ".min.js", ".map", ".lock",
}

# 出现在本文件中的域名视为「境内/内网可信」，不告警
TRUSTED_HOST_PATTERNS = (
    ".cn",            # 中国国家顶级域
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "example.com",
    "example.org",
    "example.cn",
    "w3.org",
    "schema.org",     # XML/JSON schema 命名空间
    "microsoft.com",  # 语言/框架命名空间（非外连）
    "springframework.org",
    "apache.org",
    "openjdk.org",
    "python.org",
    "vuejs.org",
    "react.dev",
    "typescriptlang.org",
)

# [规则名, 正则, 等级, 建议]
# 等级: HIGH = 阻断; MEDIUM = 告警
RULES: List[tuple] = [
    (
        "境外网络地址",
        re.compile(r"https?://[A-Za-z0-9._\-]+(?:[:]\d+)?"),
        "MEDIUM",
        "确认为业务外连还是资源引用；境外域名一律改为内网源或本地化",
    ),
    (
        "硬编码 AK/SK",
        re.compile(r"\b(?:AKIA|ASIA|LTAI)[A-Z0-9]{12,}\b"),
        "HIGH",
        "改从环境变量或配置中心读取，并立即轮换该凭据",
    ),
    (
        "疑似 OpenAI 风格密钥",
        re.compile(r"\bsk-[A-Za-z0-9\-_]{20,}\b"),
        "HIGH",
        "禁止硬编码，改从环境变量读取并轮换",
    ),
    (
        "私钥文件",
        re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
        "HIGH",
        "私钥不得进仓库，移入密钥管理系统",
    ),
    (
        "硬编码口令/令牌赋值",
        re.compile(
            r"(?i)\b(?:password|passwd|pwd|secret|token|api[_-]?key|apikey|"
            r"access[_-]?key|private[_-]?key|client[_-]?secret)\s*[:=]\s*"
            r"['\"][^'\"\s$\{]{6,}['\"]"
        ),
        "HIGH",
        "改从环境变量/配置中心读取，禁止字面量赋值",
    ),
    (
        "数据库连接串含明文口令",
        re.compile(r"(?i)\b(?:jdbc:|mongodb(?:\+srv)?://|postgres(?:ql)?://|mysql://|redis://)"
                   r"[^\s'\"]*:[^\s'\"@/]+@"),
        "HIGH",
        "口令移出连接串，改用配置中心或环境变量",
    ),
    (
        "身份证号（18 位）",
        re.compile(r"(?<!\d)[1-9]\d{5}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx](?!\d)"),
        "HIGH",
        "个人信息不得明文存储/打印，需脱敏或加密",
    ),
    (
        "中国大陆手机号",
        re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
        "MEDIUM",
        "确认是否为测试数据；生产数据需脱敏",
    ),
    (
        "疑似银行卡号",
        re.compile(r"(?<!\d)[1-9]\d{12,18}(?!\d)"),
        "LOW",
        "确认是否为卡号；如是，需脱敏存储",
    ),
    (
        "数据外发指令",
        re.compile(r"(?i)\b(?:curl|wget)\b[^\n|;&]*(?:--data|-d\s|--upload-file|-T\s)"),
        "HIGH",
        "禁止在代码中拼接外发命令，确认目标地址是否在境内",
    ),
    (
        "敏感信息写入日志",
        re.compile(r"(?i)\b(?:console\.(?:log|info|debug)|print|logger\.(?:info|debug)|log\.(?:info|debug))\s*\([^)]*"
                   r"(?:password|passwd|pwd|secret|token|idCard|id_card|idNo|phone|mobile|bankCard)"),
        "HIGH",
        "打印前必须脱敏，禁止输出完整敏感字段",
    ),
    (
        "整体对象写入日志",
        # 用 (?![\.\[]) 排除「取属性」的写法，只抓「整体对象」。
        # req.body      → 命中（整体打印，违规）
        # req.body.userId → 不命中（白名单取字段，合规）
        re.compile(r"(?i)\b(?:console\.(?:log|info|debug)|print|logger\.(?:info|debug)|log\.(?:info|debug))\s*\([^)]*"
                   r"(?:req\.body|res\.body|request\.body|response\.body"
                   r"|\buser\b|\busers\b|\breq\b|\bres\b|\bpayload\b|\bdata\b)(?![\.\[])"),
        "HIGH",
        "禁止整体打印请求/响应/用户对象，改为白名单字段并脱敏",
    ),
    (
        "境外云服务区域",
        re.compile(r"(?i)\b(?:us-east|us-west|eu-west|eu-central|ap-southeast|ap-northeast|ap-south|sa-east)-\d\b"),
        "MEDIUM",
        "云资源区域应指定为境内 region",
    ),
]

LEVEL_ICON = {"HIGH": "🔴", "MEDIUM": "🟠", "LOW": "🟡"}

# 若匹配行同时出现这些「已脱敏」信号，视为误报并跳过。
# 用于抑制「好例子被标红」——本脚本宁可漏报，也不要把正确写法判成错误。
MASK_HINTS = re.compile(
    r"(?i)(?:mask\w*|脱敏|desensitiz\w*|redact\w*|anonymiz\w*|\*{3,}|\*\*\*)"
)


class Finding(NamedTuple):
    level: str
    rule: str
    path: str
    lineno: int
    snippet: str
    advice: str


# ---------------------------------------------------------------- 工具函数

def iter_files(paths: List[str]) -> Iterator[str]:
    """展开输入路径，产出所有待扫描的普通文件路径。"""
    for raw in paths:
        if os.path.isfile(raw):
            yield raw
            continue
        if not os.path.isdir(raw):
            print(f"[warn] 路径不存在，已跳过: {raw}", file=sys.stderr)
            continue
        for root, dirs, files in os.walk(raw):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for name in files:
                if name.startswith("."):
                    continue
                if any(name.endswith(ext) for ext in SKIP_EXTS):
                    continue
                yield os.path.join(root, name)


def is_trusted_host(url: str) -> bool:
    """URL 是否命中可信/境内白名单。"""
    lowered = url.lower()
    return any(pat in lowered for pat in TRUSTED_HOST_PATTERNS)


def read_lines(path: str) -> List[str]:
    """按 UTF-8 读取，失败则忽略错误继续。"""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            return fh.read().splitlines()
    except OSError as exc:
        print(f"[warn] 无法读取 {path}: {exc}", file=sys.stderr)
        return []


def scan_text(path: str, lines: List[str]) -> List[Finding]:
    """对单个文件逐行应用规则。"""
    findings: List[Finding] = []
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        # 跳过纯注释行里的 URL（文档链接常见，噪音大）
        for rule_name, pattern, level, advice in RULES:
            for match in pattern.finditer(line):
                value = match.group(0)
                if rule_name == "境外网络地址" and is_trusted_host(value):
                    continue
                if rule_name == "疑似银行卡号" and len(value) < 15:
                    continue
                # 日志类规则：行内出现脱敏信号则视为误报，跳过
                if rule_name.endswith("写入日志") and MASK_HINTS.search(line):
                    continue
                snippet = value if len(value) <= 80 else value[:77] + "..."
                findings.append(
                    Finding(level, rule_name, path, lineno, snippet, advice)
                )
    return findings


# ---------------------------------------------------------------- 主流程

def main(argv: List[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("-")]
    if not args:
        print(__doc__)
        print("错误: 缺少扫描路径。")
        return 2

    paths = args
    files = list(iter_files(paths))
    if not files:
        print("未找到可扫描的文件。")
        return 0

    all_findings: List[Finding] = []
    for path in files:
        lines = read_lines(path)
        if lines:
            all_findings.extend(scan_text(path, lines))

    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    all_findings.sort(key=lambda f: (order.get(f.level, 9), f.path, f.lineno))

    print(f"\n扫描文件数: {len(files)}")
    print(f"发现疑似问题: {len(all_findings)}")
    print("=" * 78)

    if not all_findings:
        print("✅ 未发现数据出境或敏感信息模式匹配。")
        print("注意: 本脚本仅做模式匹配，依赖引入、云区域、遥测上报等仍需人工确认。")
        return 0

    print(f"{'等级':<6}{'文件:行号':<46}{'规则'}")
    print("-" * 78)
    for f in all_findings:
        location = f"{f.path}:{f.lineno}"
        location = location if len(location) <= 42 else "..." + location[-39:]
        print(f"{LEVEL_ICON.get(f.level, '·'):<6}{location:<46}{f.rule}")
        print(f"      片段: {f.snippet}")
        print(f"      建议: {f.advice}")
        print("-" * 78)

    high = [f for f in all_findings if f.level == "HIGH"]
    print()
    if high:
        print(f"❌ 结论: 发现 {len(high)} 项高危，必须修复后才能提交。")
        return 1

    print(f"⚠️ 结论: 无高危项，但有 {len(all_findings)} 项告警需人工确认。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
