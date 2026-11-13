# Architecture decision records

## ADR-001 — Scope the promise to available and authorized assets
**Decision:** "without export" means no need to click an Export UI when **public, permitted** file retrieval already exists. It does not mean bypassing disabled/paid exports.  
**Reason:** legitimate reproducibility, not access-control circumvention.  
**Implication:** explicit `NO_PUBLIC_ASSET` and `ENTITLEMENT_REQUIRED` statuses are successful *diagnostics*, not excuses to probe hidden APIs.

## ADR-002 — Keep retrieval separate from conversion
**Decision:** Source page → original asset → validation → optional conversion.  
**Reason:** a downloaded `.spz` must not be mislabeled as an editable mesh.  
**Implication:** no claiming Blender Edit Mode merely because a scene was saved as `.blend`.

## ADR-003 — Exact-ID extraction
**Decision:** Tripo's recovered adapter resolves `__NUXT_DATA__` references and matches the supplied item's `id` or `itemId`.  
**Reason:** selecting an unrelated recommended model is worse than a reported failure.  
**Risk:** webpage implementation changes; tests and fail-closed handling required.

## ADR-004 — Evidence-first success claims
**Decision:** Distinguish `VERIFIED` vs `FAILED` vs `NOT_TESTED` for source access, download, format checks and Blender tests.  
**Reason:** prior environments yielded materially different outcomes; a downloader script is not the asset.

## ADR-005 — Least privilege + no secret publication
**Decision:** No tokens, cookies, signed query strings or private binary models in public Git history.  
**Reason:** links and assets may contain rights or security risks; network restrictions must be respected.

## ADR-006 — Progressive rendering
**Decision:** Prioritize a 10-second 16:9 animation proof before multi-minute/multi-hour GPU jobs.  
**Reason:** de-risk rigs, textures, renderer support and GPU quotas early.

## ADR-007 — Preserve dated research without claiming it is current
**Decision:** import prior 8 Nov 2026 detailed report under `docs/RESEARCH_REPORT.md`; label pricing, features and evidence limits.  
**Reason:** onboarding benefit and future auditability, while vendors continue to change.
