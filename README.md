<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=transparent&height=120&text=Sachin%20Indwar&fontSize=48&fontAlignY=40&desc=Software%20engineer%20%C2%B7%20infrastructure%2C%20observability%2C%20open%20source&descSize=18&descAlignY=75&fontColor=e6edf3" />
  <img width="100%" alt="Sachin Indwar, software engineer working on infrastructure, observability, and open source" src="https://capsule-render.vercel.app/api?type=transparent&height=120&text=Sachin%20Indwar&fontSize=48&fontAlignY=40&desc=Software%20engineer%20%C2%B7%20infrastructure%2C%20observability%2C%20open%20source&descSize=18&descAlignY=75&fontColor=1f2328" />
</picture>

<div align="center">

I work on the tools other engineers depend on when production is on fire.

<!-- [![Portfolio](https://img.shields.io/badge/Portfolio-sachin--680.vercel.app-informational?style=flat-square&logo=vercel&logoColor=white)](https://sachin-680.vercel.app) -->
[![Email](https://img.shields.io/badge/Email-mrmister680%40gmail.com-informational?style=flat-square&logo=gmail&logoColor=white)](mailto:mrmister680@gmail.com)

</div>

---

## About me

I like infrastructure that stays boring under pressure: systems that tell you why they're
failing, recover without a human, and don't surprise the people on call.

Most of what I know came from reading other people's code. I spent a lot of time in
Kubernetes, Grafana, and OpenTelemetry source trees, trying to work out how real systems
handle the edge cases textbooks leave out. Open source is how I give some of that back. A
fix upstream reaches everyone who runs the tool, not just one team, and maintainer review
has taught me more about writing software than anything else.

I mostly write Go. I care about small, well-tested changes, clear commit history, and
leaving a codebase easier to work in than I found it.

## Things I've built

- **[Raft KV store with deterministic simulation testing](https://github.com/sAchin-680/Distributed-KV-Store-with-Raft-Deterministic-Simulation-Testing)** (Go) — a linearizable key/value store on Raft I wrote from the paper. A deterministic simulator injects partitions and crashes and can replay any failure from a single seed. Across 10,000 seeds it found 4 real consensus bugs.
- **[eBPF observability agent](https://github.com/sAchin-680/eBPF-observability-agent)** (Go) — HTTP/HTTPS request tracing with no changes to the traced app. It hooks the kernel and TLS libraries (OpenSSL, Go `crypto/tls`) and exports OpenTelemetry traces and metrics.
- **[TickLine](https://github.com/sAchin-680/TickLine)** (TypeScript) — real-time portfolio terminal with live trade streaming, FIFO P&L, and risk analytics.

## Toolbox

|                           |                                                                       |
| ------------------------- | --------------------------------------------------------------------- |
| **Languages**             | Go (primary), Python, C/C++, TypeScript                               |
| **Orchestration & IaC**   | Kubernetes, Docker, Podman, Helm, Terraform, ArgoCD, GitOps           |
| **Cloud & CI/CD**         | AWS (EC2, EKS, S3, RDS, Lambda, IAM), GitHub Actions, OIDC federation |
| **Observability**         | OpenTelemetry, Prometheus, Grafana, Loki, Jaeger, Tempo               |
| **Systems & reliability** | eBPF (CO-RE, cilium/ebpf), Linux, tc/netem chaos testing, Raft, gRPC  |
| **Data & messaging**      | PostgreSQL, MySQL, Redis, Kafka, bbolt                                |

## GitHub activity

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sAchin-680/sAchin-680/output/stats-dark.svg" />
    <img height="150" alt="GitHub stats" src="https://raw.githubusercontent.com/sAchin-680/sAchin-680/output/stats-light.svg" />
  </picture>
  &nbsp;&nbsp;
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sAchin-680/sAchin-680/output/top-langs-dark.svg" />
    <img height="150" alt="Top languages" src="https://raw.githubusercontent.com/sAchin-680/sAchin-680/output/top-langs-light.svg" />
  </picture>
  <br /><br />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sAchin-680/sAchin-680/output/streak-dark.svg" />
    <img alt="GitHub streak" src="https://raw.githubusercontent.com/sAchin-680/sAchin-680/output/streak-light.svg" />
  </picture>
</div>

---

<div align="center">

If you maintain something in this space and want a hand, or just want to talk about
observability, distributed systems, or a gnarly bug, my inbox is open.

![Profile views](https://komarev.com/ghpvc/?username=sAchin-680&style=flat-square&color=grey&label=Profile+views)

</div>
