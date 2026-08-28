---
title: Service 与网络
type: tutorial
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, Kubernetes, 网络]
---

# Service 与网络

## 学习目标
- 理解 K8s 网络模型（扁平、每个 Pod 有 IP）
- 掌握 Service 三种类型与 Ingress
- 了解 CNI 与 NetworkPolicy

## 核心概念

K8s 网络目标是：**任意 Pod 可直接互通，不使用 NAT**；Service 为动态 Pod 提供稳定虚拟 IP 与负载均衡。

## 详细说明

### 网络模型
- 每个 Pod 拥有独立 IP，Pod 间直接通信。
- 节点上的 Pod 与节点上的 Pod 也能互通。
- 由 **CNI（Container Network Interface）** 插件实现（Calico、Flannel、Cilium 等）。

### Service 类型
- **ClusterIP**（默认）：集群内部可达。
- **NodePort**：在每个节点开放固定端口。
- **LoadBalancer**：对接云厂商创建外部负载均衡器。
```yaml
apiVersion: v1
kind: Service
metadata: { name: web }
spec:
  selector: { app: web }
  ports: [{ port: 80, targetPort: 8080 }]
  type: ClusterIP
```

### Ingress
Ingress 是**七层（HTTP）路由**入口，按域名/路径转发到后端 Service：
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata: { name: web-ingress }
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service: { name: web, port: { number: 80 } }
```

### DNS 与服务发现
CoreDNS 让 Pod 可通过 `service.namespace.svc.cluster.local` 域名互相访问。

### NetworkPolicy
声明式网络访问控制（类似防火墙），限制 Pod 间流量（见 [[17-云原生安全]]）。

## 常见问题
**Q：Pod IP 会变，怎么稳定访问？**
A：永远通过 Service 的虚拟 IP / 域名访问，而不是 Pod IP。

## 参考资料
- K8s Networking / Services 官方文档

## See Also
- [[07-Kubernetes架构]]
- [[08-Pod与工作负载]]
- [[17-云原生安全]]
- [[13-服务网格ServiceMesh]]
