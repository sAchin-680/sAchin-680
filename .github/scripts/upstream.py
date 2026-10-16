#!/usr/bin/env python3
"""Rewrite the README's upstream blocks from my pull requests in other people's repos.

Usage: GH_TOKEN=... python3 upstream.py README.md
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime

USER = "sAchin-680"
# Owners whose repos are mine, so merges there are not upstream work.
EXCLUDE_OWNERS = {"sachin-680", "observax-io"}
# Upstream repos I'd rather not list.
EXCLUDE_REPOS = {
    "hashicorp/terraform-provider-aws",
    "jaegertracing/jaeger",
    "juspay/hyperswitch-control-center",
}
RECENT = 3
BLOCKS = ("UPSTREAM-SUMMARY", "UPSTREAM-RECENT")

NAMES = {
    "aws/aws-cdk": "AWS CDK",
    "google/cadvisor": "cAdvisor",
    "grafana/grafana": "Grafana",
    "kubernetes-sigs/kind": "kind",
    "kubernetes/kubernetes": "Kubernetes",
    "open-telemetry/opentelemetry-collector": "OpenTelemetry Collector",
    "podman-desktop/podman-desktop": "Podman Desktop",
    "temporalio/temporal": "Temporal",
}


def name(repo):
    return NAMES.get(repo, repo.split("/")[1])


def search_url(state):
    excluded = " ".join(
        [f"-user:{o}" for o in sorted(EXCLUDE_OWNERS)]
        + [f"-repo:{r}" for r in sorted(EXCLUDE_REPOS)]
    )
    q = f"is:pr is:{state} author:{USER} {excluded}"
    return "https://github.com/search?" + urllib.parse.urlencode({"q": q, "type": "pullrequests"})


def search(token, state):
    """Return (repo, item) for my PRs in the given state, outside excluded repos."""
    q = f"is:pr is:{state} author:{USER}"
    items, page = [], 1
    while True:
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
            {"q": q, "per_page": 100, "page": page}
        )
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
        if data.get("incomplete_results"):
            sys.exit("search returned incomplete results; leaving README unchanged")
        items += data["items"]
        if len(items) >= data["total_count"] or not data["items"]:
            break
        page += 1
    out = []
    for it in items:
        repo = it["repository_url"].split("/repos/", 1)[1]
        if repo.split("/")[0].lower() not in EXCLUDE_OWNERS and repo.lower() not in EXCLUDE_REPOS:
            out.append((repo, it))
    return out


def summary(prs, open_repos):
    counts = Counter(p["repo"] for p in prs)
    projects = " · ".join(
        f"[{name(repo)}](https://github.com/{repo}/pulls?q=is%3Apr+author%3A{USER}+is%3Amerged) ({n})"
        for repo, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    )
    links = f"[See all merged]({search_url('merged')})"
    if open_repos:
        top, n = sorted(Counter(open_repos).items(), key=lambda kv: (-kv[1], kv[0]))[0]
        links += f" · [{len(open_repos)} more in review]({search_url('open')}), including {n} in {name(top)}"
    return (
        f"**{len(prs)} pull requests merged across {len(counts)} projects:** {projects}\n\n{links}"
    )


def recent(prs, skip_urls):
    lines = ["**Recently merged**", ""]
    for p in [p for p in prs if p["url"] not in skip_urls][:RECENT]:
        title = p["title"].replace("[", "\\[").replace("]", "\\]")
        when = p["merged"].strftime("%b %Y")
        lines.append(f"- **{name(p['repo'])}** — [{title}]({p['url']}) · {when}")
    return "\n".join(lines)


def main():
    path = sys.argv[1]
    token = os.environ["GH_TOKEN"]
    readme = open(path, encoding="utf-8").read()

    prs = []
    for repo, it in search(token, "merged"):
        merged_at = (it.get("pull_request") or {}).get("merged_at")
        if not merged_at:
            continue
        prs.append({
            "repo": repo,
            "title": it["title"].strip(),
            "url": it["html_url"],
            "merged": datetime.fromisoformat(merged_at.replace("Z", "+00:00")),
        })
    if not prs:
        sys.exit("no upstream pull requests found; leaving README unchanged")
    prs.sort(key=lambda p: p["merged"], reverse=True)

    # PRs already linked by hand elsewhere in the README stay out of the recent list.
    pattern = re.compile(r"(<!-- (UPSTREAM-\w+):START -->\n)(?:.*?\n)?(<!-- \2:END -->)", re.S)
    if sorted(m.group(2) for m in pattern.finditer(readme)) != sorted(BLOCKS):
        sys.exit(f"{path} must contain each of {BLOCKS} exactly once")
    outside = pattern.sub("", readme)
    skip_urls = set(re.findall(r"https://github\.com/[^)\s]+/pull/\d+", outside))

    open_repos = [repo for repo, _ in search(token, "open")]
    content = {
        "UPSTREAM-SUMMARY": summary(prs, open_repos),
        "UPSTREAM-RECENT": recent(prs, skip_urls),
    }
    updated = pattern.sub(lambda m: m.group(1) + content[m.group(2)] + "\n" + m.group(3), readme)
    if updated != readme:
        open(path, "w", encoding="utf-8").write(updated)
        print(f"updated: {len(prs)} merged upstream pull requests")
    else:
        print("no change")


if __name__ == "__main__":
    main()
