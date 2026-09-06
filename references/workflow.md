# End-to-end workflow

## 1. Freeze history and define coverage

Use merge ancestry for sequence. PR numbers and commit timestamps can be out of
order. Resolve the endpoint to a full SHA and retain subjects/PR metadata.
Choose sampled or exhaustive coverage explicitly. Pin visual milestones instead
of relying exclusively on uniform intervals; sample across the entire range.
Do not assume a hosted preview still represents a PR without revision evidence.

Discover pages separately in each revision. Understand framework route groups,
dynamic parameters, redirects, feature flags, roles, and representative IDs.
Use stable logical IDs when routes move. A static route list is not full coverage
of dialogs, user roles, detail records, scroll positions, or workflow states.
For disabled or inaccessible surfaces, document why they are excluded. Do not
apply another project's route exclusions to this one.

## 2. Build one faithful vertical slice

Prove earliest and current snapshots, plus a middle revision if the stack changed.
Keep application-specific setup in a repository adapter:

- `prepare(revision)`: isolated exact source, locked dependencies, runtime mode.
- `startData(revision)`: matching backend/schema or explicit static/no-backend mode.
- `seed(revision)`: compatible deterministic fixtures, with no real outbound effects.
- `startApp(revision, data)`: explicit ports/origins, readiness, ownership, cleanup.
- `authenticate(page)`: actual supported session for the intended role/workspace.
- `routes(revision)`: logical ID, path, navigation steps, and readiness evidence.

These are responsibilities, not a mandatory SDK. Adapt existing project tooling.
For each route, use real links/buttons when full reloads trigger historical auth
races. Check the final origin/path, loaded app-specific heading/data, settled
spinners/skeletons, fonts, and viewport-visible images. Capture a fixed viewport
and browser configuration. Keep errors and failed screenshots for diagnosis,
separate from successful assets. Record any recovery through actual app actions.

## 3. Persist evidence and scale

Useful manifest fields:

- source SHA, PR/subject, source verification, tool/browser versions;
- matching backend revision/hash or explicit no-backend explanation;
- fixture version, runtime/build mode, auth role, reconstruction exceptions;
- viewport, requested and observed route, readiness observations, links;
- screenshot relative path and SHA-256, attempts, and final status;
- planned route inventory and a run-level `completed` flag.

Keep private runtime details separate from portable delivery evidence. Do not
copy secrets, cookies, or private logs into the player folder.

Once the slice works, process a bounded queue. Cache dependencies/builds only
when keys cover source revision, runtime/build mode, and embedded public config
such as API origins. Verify reused source. Use fresh isolated data for retries
unless the adapter proves its fixture is idempotent. Save progress atomically
per page and revision. Resume verified successes; do not accept incomplete runs.
Handle a changed plan without treating obsolete failed entries as active failures.

## 4. Compose a stable atlas

Use a deterministic canvas or equivalent compositor rendered through a browser,
then encode frames with FFmpeg. Keep the player driven by the same timeline so
video and interactive results agree. The compositor may resize real screenshots;
it must not reconstruct or repaint their application content.

Allocate stable slots by logical page identity, with sensible parent/group
placements. Preserve those slots across revisions; derive a monotonic zoom-out
from cumulative bounds if the user wants continuous growth. Removed pages can
leave gaps. A layout that repacks constantly makes design changes hard to follow.
Use contextual observed navigation edges; global sidebar links can overwhelm it.

Map all milestones into the requested total duration. A 60-second, 52-snapshot
cut gives roughly 1.15 seconds per snapshot; a 90-second cut gives 1.73 seconds.
Keep crossfades short relative to a milestone. Define camera keyframes in time
order and format playback time correctly past one minute.

Use real brand assets supplied by the project. Keep wordmark, PR title/number,
logo, and optional date/count/footer independently controllable. Fit long PR
names; avoid timeline label collisions near the final marker. Default to concise
presentation; do not add provenance slogans to the canvas when evidence can
live in the accompanying manifest. Respect the user's chosen overlay content.

For thousands of screenshots, use appropriately sized derivatives for the atlas
while retaining original pixels and hashes. Bound decoded-image memory or load
only nearby stages if the browser cannot hold the complete history.

## 5. Validate and deliver

Before encoding, check the requested sequence, full SHAs, capture completion,
source/backend matching where required, image hashes, and real file existence.
Reject mislabeled or incomplete evidence. In a gap-tolerant film, represent gaps
explicitly and keep them distinct from app screenshots.

Inspect opening, middle, growth/removal transitions, long PR names, and final
layout. Verify the MP4 with ffprobe and a full FFmpeg decode, not just a file-size
check. Exercise play/pause, end-of-film time, and scrubbing in the offline player;
check browser errors and local asset loading. Keep the original approved cut
when making a revision. Report actual counts and scope, with direct output links.

Presentation edits should normally touch only the compositor and reuse validated
captures. A new visual preference does not justify another historical capture
batch unless it changes the underlying viewport or required application states.
