<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=transparent&height=120&text=Sachin%20Indwar&fontSize=48&fontAlignY=40&desc=Software%20engineer%20%C2%B7%20open%20source&descSize=18&descAlignY=75&fontColor=e6edf3" />
  <img width="100%" alt="Sachin Indwar, software engineer and open source contributor" src="https://capsule-render.vercel.app/api?type=transparent&height=120&text=Sachin%20Indwar&fontSize=48&fontAlignY=40&desc=Software%20engineer%20%C2%B7%20open%20source&descSize=18&descAlignY=75&fontColor=1f2328" />
</picture>

<div align="center">

I build and fix the tools platform teams run: observability, containers, consensus.

<!-- [![Portfolio](https://img.shields.io/badge/Portfolio-sachin--680.vercel.app-informational?style=flat-square&logo=vercel&logoColor=white)](https://sachin-680.vercel.app) -->
[![Email](https://img.shields.io/badge/Email-mrmister680%40gmail.com-informational?style=flat-square&logo=gmail&logoColor=white)](mailto:mrmister680@gmail.com)

</div>

---

## About me

I like infrastructure that stays boring under pressure: systems that explain their own
failures, recover without a human, and don't surprise the people on call. I mostly write Go,
and most of my work goes upstream, where one fix reaches everyone who runs the tool.

## Upstream

<!-- UPSTREAM-SUMMARY:START -->
**35 pull requests merged across 4 projects:** [Podman Desktop](https://github.com/podman-desktop/podman-desktop/pulls?q=is%3Apr+author%3AsAchin-680+is%3Amerged) (23) · [Grafana](https://github.com/grafana/grafana/pulls?q=is%3Apr+author%3AsAchin-680+is%3Amerged) (7) · [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector/pulls?q=is%3Apr+author%3AsAchin-680+is%3Amerged) (3) · [AWS CDK](https://github.com/aws/aws-cdk/pulls?q=is%3Apr+author%3AsAchin-680+is%3Amerged) (2)

[See all merged](https://github.com/search?q=is%3Apr+is%3Amerged+author%3AsAchin-680+-user%3Aobservax-io+-user%3Asachin-680+-repo%3Ahashicorp%2Fterraform-provider-aws+-repo%3Ajaegertracing%2Fjaeger+-repo%3Ajuspay%2Fhyperswitch-control-center&type=pullrequests) · [19 more in review](https://github.com/search?q=is%3Apr+is%3Aopen+author%3AsAchin-680+-user%3Aobservax-io+-user%3Asachin-680+-repo%3Ahashicorp%2Fterraform-provider-aws+-repo%3Ajaegertracing%2Fjaeger+-repo%3Ajuspay%2Fhyperswitch-control-center&type=pullrequests), including 5 in Kubernetes
<!-- UPSTREAM-SUMMARY:END -->

**Highlights**

- **Podman Desktop** — telemetry now turns itself off when it detects a CI environment, so pipelines no longer have to disable it by hand ([#19266](https://github.com/podman-desktop/podman-desktop/pull/19266)).
- **Grafana** — fixed panels rendering blank when the legend display mode is hidden ([#134866](https://github.com/grafana/grafana/pull/134866)).
- **OpenTelemetry Collector** — component authors can declare feature gates in `metadata.yaml` and `mdatagen` generates their documentation ([#14130](https://github.com/open-telemetry/opentelemetry-collector/pull/14130)).

<!-- UPSTREAM-RECENT:START -->
**Recently merged**

- **Podman Desktop** — [chore(extension-api): publish only the type declaration files](https://github.com/podman-desktop/podman-desktop/pull/19654) · Oct 2026
- **Grafana** — [Annotations: Keep annotation ids as strings and drop id from the legacy PUT body](https://github.com/grafana/grafana/pull/121248) · Sep 2026
- **Podman Desktop** — [feat(ci): publish @podman-desktop/api-mocks-vitest to npmjs](https://github.com/podman-desktop/podman-desktop/pull/19365) · Sep 2026
<!-- UPSTREAM-RECENT:END -->

## Things I've built

- **[Raft KV store with deterministic simulation testing](https://github.com/sAchin-680/Distributed-KV-Store-with-Raft-Deterministic-Simulation-Testing)** (Go) — a linearizable key/value store on Raft I wrote from the paper. A deterministic simulator injects partitions and crashes and can replay any failure from a single seed. Across 10,000 seeds it found 4 real consensus bugs.
- **[eBPF observability agent](https://github.com/sAchin-680/eBPF-observability-agent)** (Go) — HTTP/HTTPS request tracing with no changes to the traced app. It hooks the kernel and TLS libraries (OpenSSL, Go `crypto/tls`) and exports OpenTelemetry traces and metrics. Adds +0.65 ms p50 latency at 1,000 req/s, and one binary runs on kernels 5.15 and 6.8.

## Toolbox

|                                |                                            |
| ------------------------------ | ------------------------------------------ |
| **Languages**                  | Go, Python, TypeScript                     |
| **Containers & orchestration** | Kubernetes, Docker, Helm                   |
| **Cloud, IaC & CI/CD**         | AWS, Terraform, GitHub Actions, ArgoCD     |
| **Observability**              | OpenTelemetry, Prometheus, Grafana, Jaeger |
| **Systems**                    | Linux, eBPF, gRPC                          |
| **Data**                       | PostgreSQL, Redis, Kafka                   |

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
