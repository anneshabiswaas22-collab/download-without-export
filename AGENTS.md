# Agent instructions — Download Without Export

Read `README.md`, `docs/HANDOFF.md`, `docs/EVIDENCE_LOG.md`, `docs/ARCHITECTURE.md` and `docs/ROADMAP.md` first. This file is the entry point for Codex and other coding agents.

## Product goal
Build a dependable, auditable and **permission-respecting** tool that retrieves a genuinely accessible 3D asset from a public or owner-authorized model/world page without needing to click an Export UI, verifies it and optionally helps transform it into Blender-editable geometry and a short animation preview.

## Current state
- Tripo study case: `e3bca070-3984-4aa3-8d54-1192acc9da1e`; old `scripts/tripo/download_tripo_model.py` is a proof of concept, not a production-ready app.
- Marble study case: `608d6222-8bb9-4575-8845-b1efd2f980ab`; two viewer URLs, same world; historical SPZ success **reported**, no reproducible downloader in repo.
- Earlier `Taj_Mahal.fbx`, resort `.spz` and `.blend` assets are **not in this repository**.
- Our reconstructed research and evidence have explicit verification limits. Never state a new tool run succeeded unless it actually did.

## Implementation contract
1. **Never** bypass login, paid/export entitlement, DRM, rate limits, robots/security policy, network/proxy restrictions or other access controls. Report blocked outcomes; authorized alternatives are preferable to workarounds.
2. Work on only user-owned, openly licensed or otherwise **authorized** material. Do not publish third-party binaries, private data or signed URLs.
3. Keep separate layers: page resolution → authorized download → bytes/signature → structural validation → Blender import → editability → rig/animation → rendering.
4. Match exact model/world IDs; fail closed if ambiguous; never select the first related model.
5. Treat format/structure accurately: SPZ splats are **not** selectable polygon furniture; a `.blend` can contain splats.
6. Avoid SSRF, query-token logging, unsafe redirects, arbitrary file execution and unbounded downloads in all new network-facing code.
7. Prefer small dependency-free unit tests with synthetic fixtures; actual vendor requests must be opt-in and documented with their permission basis.
8. Record verified/failed/not-tested at each stage, and list Blender version, output hash, bytes, geometry/material/rig counts if truly checked.
9. After code changes run `python -m unittest discover -s tests -v` and update docs/tests as needed.
10. Do not claim GPU notebook availability or vendor free-tier/plan rights without checking current official sources.

## Priority sequence
M1 exact Tripo resolver and hardening → M2 allowed Marble SPZ reproduction, then Blender validation → M3 stable CLI/manifests/security → M4 editable mesh/scene and 10-second video proof → M5 Colab/Kaggle workflows. See `docs/ROADMAP.md`.

## PR checklist
Summarize outcome, tests actually executed, files changed, exact authorization basis, failure handling and remaining unknowns. Keep code and README consistent. Ask for a permitted access configuration rather than attempting a security bypass.
