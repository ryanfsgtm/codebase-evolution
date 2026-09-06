#!/usr/bin/env python3
"""Freeze a sampled or complete first-parent visual-history plan; no Git mutations."""
import argparse
import json
import subprocess
from pathlib import Path


def git(repo, *args):
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True, stderr=subprocess.PIPE
    ).strip()


def resolve(repo, ref):
    return git(repo, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")


def plan(repo, ref="HEAD", samples=50, exhaustive=False, pins=(), basis="auto"):
    import re
    if samples < 2:
        raise ValueError("samples must be at least 2")
    endpoint = resolve(repo, ref)
    rows = git(repo, "log", "--first-parent", "--reverse",
               "--format=%H%x00%cI%x00%s", endpoint).splitlines()
    history = []
    for row in rows:
        sha, date, subject = row.split("\0", 2)
        numbers = re.findall(r"#(\d+)", subject)
        history.append(dict(sha=sha, date=date, subject=subject,
                            pr=int(numbers[-1]) if numbers else None))
    prs = [row for row in history if row["pr"] is not None]
    actual_basis = ("prs" if prs else "commits") if basis == "auto" else basis
    candidates = prs if actual_basis == "prs" else history
    if not candidates:
        raise ValueError("No PR numbers found in first-parent subjects; use --basis commits or supply PR metadata with an adapter")
    count = min(samples, len(candidates))
    if exhaustive or count == 1:
        selected = {row["sha"] for row in candidates}
    else:
        selected = {candidates[round(i * (len(candidates) - 1) / (count - 1))]["sha"]
                    for i in range(count)}
    selected.add(endpoint)
    history_shas = {row["sha"] for row in history}
    pinned = []
    for ref_to_pin in pins:
        sha = resolve(repo, ref_to_pin)
        if sha not in history_shas:
            raise ValueError(f"Pinned revision {ref_to_pin!r} is outside the endpoint's first-parent history")
        selected.add(sha)
        pinned.append(sha)
    milestones = [row for row in history if row["sha"] in selected]
    return {
        "through": history[-1],
        "selection": {
            "basis": actual_basis,
            "method": "all-first-parent-candidates" if exhaustive else "uniform-first-parent-sample",
            "requestedSamples": None if exhaustive else samples,
            "candidateCount": len(candidates),
            "selectedCount": len(milestones),
            "allCandidatesSelected": all(row["sha"] in selected for row in candidates),
            "pins": pinned,
            "prNumberSource": "last #number in Git commit subject" if actual_basis == "prs" else None,
        },
        "selectionNotes": [
            "Sequence follows first-parent Git ancestry, not timestamps or PR-number order.",
            "The frozen endpoint is included even when it is not itself a PR-labeled commit.",
            "PR-subject parsing depends on this repository's merge conventions; verify against PR metadata when needed.",
        ],
        "milestones": milestones,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--ref", default="HEAD")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--samples", type=int, default=50)
    mode.add_argument("--all", action="store_true", dest="exhaustive")
    parser.add_argument("--basis", choices=("auto", "prs", "commits"), default="auto")
    parser.add_argument("--pin", action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true", help="Replace an existing plan")
    args = parser.parse_args()
    if args.output.exists() and not args.force:
        parser.error("Output exists; use another filename or --force to replace the frozen plan")
    try:
        result = plan(args.repo, args.ref, args.samples, args.exhaustive, args.pin, args.basis)
    except (ValueError, subprocess.CalledProcessError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w" if args.force else "x") as output:
        output.write(json.dumps(result, indent=2) + "\n")
    print(f"Wrote {len(result['milestones'])} milestones through {result['through']['sha'][:12]} to {args.output}")


if __name__ == "__main__":
    main()
