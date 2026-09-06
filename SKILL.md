---
name: codebase-evolution
description: Create or revise app-development timelapse videos and interactive page atlases using real browser screenshots of historical Git or PR revisions. Use for visual histories of an app, including page growth, redesigns, and navigation flows.
---

# Codebase evolution

Produce a reproducible video and scrub-able atlas whose application pixels come
from actual browser renders of the selected revisions. The task includes getting
historical apps running, validating captures, composing the film, and delivering
working artifacts; a storyboard alone does not complete a generation request.

## Choose the work needed

- **New history:** inspect repository instructions, app architecture, scripts,
  dependency locks, route conventions, auth, and data requirements. Read
  [the end-to-end workflow](references/workflow.md). Start with a small proof
  before expanding the batch.
- **Broken capture:** read [reconstruction and debugging](references/reconstruction.md).
  Diagnose whether source, dependencies, runtime, authentication, data, navigation,
  or readiness failed. A screenshot of an error or spinner is not a successful page.
- **Video edit:** use existing verified captures when only duration, labels,
  branding, layout, or camera movement changed. Re-render and verify the result;
  do not repeat historical builds or change app screenshots unnecessarily.

Implement the capture and rendering tooling in the target repository, adapting
its routes, authentication, backend, fixtures, and branding. The workflow reference
defines those responsibilities without assuming a particular application.

## Establish the capture contract

Infer scope and visual preferences from the conversation and repository. Resolve
only material missing choices: revision range, sampled versus every revision,
route/state coverage, authentication/data access, and desired output duration.
Explain what is being sampled. “From PR 1 to today” specifies endpoints, not
necessarily permission to silently replace an explicit request for every PR with
a sparse sample. Freeze the endpoint SHA so new merges do not extend a running job.

For a starting point when unspecified: approximately 50 representative milestones,
60–90 seconds, desktop screenshots, a stable page atlas, and an offline scrubber.
Use existing branding and the user's preferred density of labels. These are
starting choices, not requirements. Clearly distinguish overlay dates/text from
text already present inside authentic application screenshots.

The dependency-free `scripts/plan_history.py` can freeze a first-parent history:

```sh
python <skill-dir>/scripts/plan_history.py --repo <repo> --ref HEAD --samples 50 --output <plan.json>
```

Use `--all` instead of `--samples` for all candidates, and `--pin <ref>` to preserve
important milestones. The output identifies its sampling method and candidates.
Repositories with different merge conventions may need a PR-metadata adapter;
do not infer missing PR numbers or historical deployment contents.

## Evidence and execution rules

- Attribute each screenshot to its real source revision. Keep matching backend
  source when required. Treat fixtures and infrastructure adaptations as explicit
  reconstruction choices. Do not patch historical UI and present it as original.
- Build in isolated archives/worktrees and use the revision's lockfile. Use an
  isolated data store where needed. Existing authorization applies; this skill
  does not grant permission to mutate shared services, send messages, deploy,
  commit, or publish. Synthetic identities may still create persistent external
  records: handle that within the user's actual authorization.
- Prefer a dependable real-browser capture runner, such as standalone Playwright,
  where available and permitted. Preserve other applicable tool instructions;
  this skill does not override browser access constraints.
- Store private configuration outside committed files. Keep tokens and auth-state
  files out of the skill, shared artifacts, and logs intended for delivery.
- Validate a small early/middle/latest set before launching a large batch. Save
  atomic progress and completed manifests. Limit concurrency to available resources.
  Retry transient failures with a bound; investigate repeated identical failures.
- Record genuine unrenderable revisions and sampling substitutions. If every PR
  was requested, retain a visible/explicit gap report instead of silently dropping
  revisions. Never fabricate missing screens or substitute later pixels under an
  earlier label.
- Use stable page identities and positions. Show removed pages disappearing;
  avoid carrying their last screenshot forward as if still present. Edges need
  observed links or exercised navigation, not guesses about business workflows.

## Finish

Verify source/image provenance, complete planned coverage (or disclosed gaps),
video duration/resolution/frame count and full decode, offline player controls,
and representative opening/middle/final frames. Run focused checks for changed
code and the repository's applicable gates. Preserve earlier approved outputs
when creating a new cut. Deliver the video and player links, actual coverage,
and any meaningful limitations. Do not claim every page, PR, or workflow was
captured unless the evidence supports it.
