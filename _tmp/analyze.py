import os, re, json, math, difflib
from collections import defaultdict, Counter
from datetime import date

WIKI = r"E:/999知识库/wiki"
TODAY = date(2026, 9, 11)
THRESH = 14

# gather, key by REL PATH (unique)
files = {}
for dp, dn, fn in os.walk(WIKI):
    for f in fn:
        if f.endswith(".md"):
            full = os.path.join(dp, f).replace("\\", "/")
            rel = os.path.relpath(full, WIKI).replace("\\", "/")
            base = f[:-3]
            files[rel] = {"base": base, "path": full, "backup": "_旧版备份" in rel, "rel": rel}

# basename -> list of rel
base_index = defaultdict(list)
for rel, info in files.items():
    base_index[info["base"]].append(rel)

def resolve(t):
    """Resolve a link target (basename) to a rel path. Prefer active; else backup; else None."""
    cands = base_index.get(t, [])
    if not cands:
        return None
    act = [c for c in cands if not files[c]["backup"]]
    if act:
        return act[0] if len(act) == 1 else ("AMBIG:" + "|".join(act))
    return cands[0]

link_re = re.compile(r'(?<!!)\[\[([^\]\|#]+)(?:[#\|][^\]]*)?\]\]')
embed_re = re.compile(r'!\[\[([^\]]+)\]\]')

def parse_fm(text):
    fm = {}; body = text
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.S)
    if m:
        fm_text = m.group(1); body = text[m.end():]
        for line in fm_text.split('\n'):
            if ':' in line:
                k, v = line.split(':', 1); fm[k.strip()] = v.strip()
    return fm, body

def datediff(dstr):
    if not dstr: return None
    try:
        y, mo, d = dstr.split('-'); return (TODAY - date(int(y), int(mo), int(d))).days
    except Exception:
        return None

active = {r: i for r, i in files.items() if not i["backup"]}
pages_stats = {}
inlinks = Counter()
dead_links = defaultdict(list)
embed_uses = defaultdict(list)

for rel, info in files.items():
    text = open(info["path"], encoding="utf-8", errors="ignore").read()
    fm, body = parse_fm(text)
    links = link_re.findall(text)
    embeds = embed_re.findall(text)
    is_log = (info["base"] == "log")
    for t in links:
        t = t.strip()
        r = resolve(t)
        if r and not r.startswith("AMBIG"):
            if r in active:
                inlinks[r] += 1
        else:
            dead_links[t].append((rel, is_log))
    for e in embeds:
        et = e.split('|')[0].split('#')[0].strip()
        embed_uses[et].append(rel)
    # stub: very short body OR explicit placeholder marker
    marker = bool(re.search(r'占位页|本文待补|（待补）|\(待补\)|待补录|待补内容|待撰写', body))
    pages_stats[rel] = {
        "base": info["base"], "backup": info["backup"], "bodysize": len(body.strip()),
        "marker": marker, "nlinks": len(links),
        "created": fm.get("created", ""), "updated": fm.get("updated", ""),
        "title": fm.get("title", info["base"]), "type": fm.get("type", ""),
    }

orphans = [r for r in active if inlinks[r] == 0 and r not in ("index.md", "log.md")]
orphans.sort()

stubs = []
for r, s in active.items():
    if pages_stats[r]["bodysize"] < 300 or pages_stats[r]["marker"]:
        dd = datediff(pages_stats[r]["updated"]) or datediff(pages_stats[r]["created"])
        longterm = (dd is not None and dd > THRESH)
        stubs.append((r, pages_stats[r]["bodysize"], pages_stats[r]["marker"], pages_stats[r]["updated"] or pages_stats[r]["created"], longterm, dd))
stubs.sort(key=lambda x: (-int(x[4]), x[3]))

# dead links
dead_real = {}; dead_hist = {}
for t, srcs in dead_links.items():
    log_srcs = [s for s, lg in srcs if lg]
    oth = [s for s, lg in srcs if not lg]
    if oth: dead_real[t] = oth
    if log_srcs: dead_hist[t] = log_srcs

def infer(t):
    best, bestr, second = None, 0.0, 0.0
    for cand in active:
        c = active[cand]["base"]
        if c == t: continue
        rr = difflib.SequenceMatcher(None, t, c).ratio()
        if rr > bestr:
            second = bestr; bestr = rr; best = cand
        elif rr > second:
            second = rr
    if best and bestr >= 0.85 and (bestr - second) >= 0.12:
        return best, round(bestr, 2)
    return None, round(bestr, 2)

infer_map = {t: list(infer(t)) for t in dead_real}

print("===== 规模 =====")
print("总 md:", len(files), "| 活跃:", len(active), "| 备份:", sum(1 for s in files.values() if s['backup']))
themes = Counter(os.path.dirname(r) for r in active)
print("活跃目录:", dict(themes))

print("\n===== 1) 孤儿页(活跃,无入链) =====")
print("数量:", len(orphans))
for r in orphans:
    print("  ", r, "| title:", pages_stats[r]["title"], "| size:", pages_stats[r]["bodysize"])

print("\n===== 1b) 疑似 stub =====")
print("数量:", len(stubs))
for r, sz, mk, dt, lt, dd in stubs:
    print(f"  {r:42s} size={sz:6d} marker={int(mk)} date={dt} days={dd} longterm={lt}")

print("\n===== 2) 真实断链(活跃内容页) =====")
print("数量:", len(dead_real))
for t, srcs in sorted(dead_real.items()):
    cand, sc = infer_map[t]
    print(f"  [[{t}]]  occ={len(srcs)}  infer={cand}({sc})")
print("-- log.md 历史引用(保留):", len(dead_hist))
for t, srcs in sorted(dead_hist.items()):
    print(f"  [[{t}]] x{len(srcs)}")

print("\n===== 2b) 嵌入图目标数 =====", len(embed_uses))

# overlap: char-2gram tf-idf cosine over active
def shingles(txt, n=2):
    txt = re.sub(r'\s+', '', txt)
    return [txt[i:i+n] for i in range(len(txt)-n+1)]
docs = {}
for r in active:
    text = open(files[r]["path"], encoding="utf-8", errors="ignore").read()
    _, body = parse_fm(text)
    body = re.sub(r'```.*?```', '', body, flags=re.S)
    body = re.sub(r'!?\[\[[^\]]*\]\]', '', body)
    docs[r] = body[:5000]
df = defaultdict(int); tf = {}
for r, txt in docs.items():
    c = Counter(shingles(txt)); tf[r] = c
    for k in c: df[k] += 1
N = len(docs)
def normvec(r):
    c = tf[r]; vec = {}
    for k, v in c.items():
        idf = math.log((N+1)/(df[k]+1)) + 1
        vec[k] = (1+math.log(v))*idf
    nrm = math.sqrt(sum(x*x for x in vec.values())) or 1
    return {k: v/nrm for k, v in vec.items()}
nv = {r: normvec(r) for r in docs}
pairs = []
ks = list(docs.keys())
for i in range(len(ks)):
    for j in range(i+1, len(ks)):
        a, b = ks[i], ks[j]
        inter = set(nv[a]) & set(nv[b])
        if not inter: continue
        dot = sum(nv[a][k]*nv[b][k] for k in inter)
        if dot > 0.4:
            pairs.append((round(dot,3), a, b))
pairs.sort(reverse=True)
print("\n===== 4) 内容重叠(cosine>0.4, top 20) =====")
for sim, a, b in pairs[:20]:
    print(f"  {sim:.3f}  {a}  <->  {b}")

out = {
    "total": len(files), "active": len(active), "backup": sum(1 for s in files.values() if s['backup']),
    "themes": dict(themes),
    "orphans": [{"rel": r, "title": pages_stats[r]["title"], "size": pages_stats[r]["bodysize"]} for r in orphans],
    "stubs": [{"rel": r, "size": sz, "marker": mk, "date": dt, "longterm": lt} for r, sz, mk, dt, lt, dd in stubs],
    "dead_real": dead_real, "dead_hist": dead_hist,
    "infer_map": infer_map,
    "overlap": [[sim, a, b] for sim, a, b in pairs[:20]],
}
json.dump(out, open(r"E:/999知识库/_tmp/health_analysis.json", "w"), ensure_ascii=False, indent=2)
print("\n[done] -> _tmp/health_analysis.json")
