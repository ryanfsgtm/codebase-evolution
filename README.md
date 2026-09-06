# Codebase Evolution

A Codex skill for producing app-development timelapse videos and interactive
page atlases from real browser screenshots of historical Git/PR revisions.

It guides the complete workflow: select revisions, reconstruct historical apps,
seed isolated data, capture real pages, compose a stable page map, and verify
the finished video and offline player.

## Install

Clone this repository into your local skills directory:

```sh
git clone https://github.com/ryanfsgtm/codebase-evolution.git ~/.codex/skills/codebase-evolution
```

If you use a custom `CODEX_HOME`, place it in that directory's `skills/` folder.

## Use

```text
Use $codebase-evolution to create a 60-second development atlas of this app,
from its first PR through today, using real browser screenshots and the
project's branding.
```

The skill also supports editing an existing film without recapturing the app.
Specify whether you want every revision or a representative sample.

## Contents

- [SKILL.md](SKILL.md): the workflow and invocation guidance.
- [History planner](scripts/plan_history.py): dependency-free Python tooling for
  sampled or exhaustive first-parent plans, frozen endpoints, and pinned refs.
- [Workflow reference](references/workflow.md): capture evidence, batching,
  composition, and delivery checks.
- [Debugging reference](references/reconstruction.md): practical lessons from
  real historical app reconstruction.

## Plan a history

```sh
python3 scripts/plan_history.py --repo /path/to/app --samples 50 --output /path/to/plan.json
python3 scripts/plan_history.py --repo /path/to/app --all --output /path/to/all-revisions.json
```

Use `--pin <ref>` to preserve milestones and `--basis commits` for repositories
without PR numbers in their merge subjects. Existing plans are preserved unless
`--force` is supplied. Planning requires Python 3 and Git; capture/render runtime
requirements depend on the app and adapter.

## What is reusable

The workflow, evidence requirements, history planner, and composition approach
transfer across apps. Capture and rendering tooling is implemented in the target
repository with adapters for its routes, authentication, backend, fixtures, and
branding.

This repository contains the skill, generic planner, and supporting documentation.
It includes no application-specific code, logos, credentials, captured screenshots,
or historical application archives.
