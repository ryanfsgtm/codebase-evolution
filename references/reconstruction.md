# Reconstruction and debugging

These are observed failure classes from a Next.js/Clerk/Convex reconstruction,
not universal requirements for every application. Diagnose before applying a fix.

| Symptom | Evidence to inspect | Appropriate response |
| --- | --- | --- |
| Screenshot stays on a spinner | network, backend logs, CSP, auth/session and fixture state | Fix the cause; a visible shell alone is insufficient readiness. |
| Auth works over HTTPS but not HTTP | cookie Secure/SameSite attributes and actual origin | Use a disposable trusted-exception browser context and consistent local HTTPS where necessary; do not change system trust. |
| TLS “wrong version” through a proxy | whether Next self-proxies back to an HTTP upstream with an HTTPS origin | A direct HTTPS server using that revision's installed Next can avoid the loop. |
| Strict CSP blocks an isolated backend | effective `connect-src`, including `default-src` fallback | Extend only the necessary loopback HTTP/WS origins and document the exception. Preserve nonces and other directives. |
| A framing-only CSP breaks sign-in after a local adjustment | no original `connect-src` or `default-src` | Connections were unrestricted. Do not add a new restrictive connection policy. |
| Historical release build fails unrelated type/prerender gates | build logs and framework version's supported modes | A documented compile-only mode may reconstruct a real app; it does not establish historical release validity. Avoid source patches disguised as original code. |
| Data pages run queries before auth arrives | error boundary versus stable session; hard reload versus SPA transition | Follow real links; expand collapsed sidebar groups using actual buttons. Use a bounded real “Try Again” recovery if the app offers it. |
| Link exists but cannot be clicked | hidden mobile duplicates or collapsed desktop groups | Choose a visible desktop target; expand its group. Do not blindly take the first DOM match. |
| Compare/New navigation changed over time | actual revision's anchor/button markup | Prefer the real link if available, otherwise click the version's actual button and verify the destination. |
| Modules disappear or show upgrade gates unexpectedly | effective fixture entitlement in that revision | Seed a valid isolated entitlement through historical APIs; catalog IDs and argument shapes may have changed. Never call real billing to simulate a paid account. |
| An apparent page navigates elsewhere | server redirect or client router replacement returning no page | Exclude the alias or capture its destination under the actual destination identity; re-check URL after readiness. |
| Waiting for images never ends | offscreen lazy-loaded images | Wait for fonts and viewport-visible image decoding with a bound. |
| Partial run looks complete after interruption | run completion flag versus per-route checkpoint | Require explicit run completion and planned coverage before accepting it. |
| Large atlas crashes the renderer | decoded image memory, not just PNG file sizes | Downsample compositor derivatives and/or load neighboring epochs. Preserve original hashes. |

Keep diagnostic error messages useful but redact credentials and session tokens.
An error in the capture setup and an actual historical application defect are
not the same thing. If a historical revision has a reproducible application defect
and the next revision fixes it, a sampled film may use the real fixed revision
with an explicit sampling note. Do not patch the broken revision or relabel the
replacement's screenshots. Keep project-specific substitutions in that project's
plan, rather than making them defaults for other repositories.

For each repeated failure, preserve the minimal evidence and choose a concrete
hypothesis. Retry transient operations with a bound (often two retries). Do not
spend unlimited retries on an identical deterministic error. Validate a fix on
the affected slice before expanding to the full batch again.
