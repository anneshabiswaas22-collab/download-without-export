# Roadmap and first contribution tasks

**State as of 13 Nov 2026:** GitHub handoff and legacy script/research imported; currently **not** an end-to-end product. The recovered original binary assets have not been imported. No new live provider test was conducted during documentation.

## M0 — Contributor-ready handoff

- [x] Public repository, README, goals, legacy findings, limitations, safety policy
- [x] Recovered Tripo downloader source and dated image-to-3D research
- [x] Offline asset-header/hash inspector and synthetic unit tests
- [ ] Run CI on the published commit; inspect job output
- [ ] Choose and pin packaging/version-management strategy

**Acceptance:** a new developer can understand the purpose, reproduce offline tests, and identify known blockers without reading the original chat.

## M1 — Reproduce Tripo authorized case

- [ ] Obtain current permission basis to download the **exact** public model
- [ ] Test source page, precise indexed Nuxt extraction and CDN redirect in allowed environment
- [ ] Replace legacy hardcoded model ID with safe CLI arguments and strong host validation
- [ ] Add a synthetic fixture for multiple related models and ambiguous fields
- [ ] Use streaming downloads, retries/backoff, atomic rename, SHA-256 and error redaction
- [ ] Document file format, sizes, missing texture dependencies, Blender version and mesh/material/armature metrics
- [ ] Store **metadata, hashes, screenshots where rights permit**; avoid committing the 3D binary without redistribution rights

**Acceptance:** real local asset returned for permitted source; checks L0-L4 recorded, or exact block reported without false success.

## M2 — Reproduce Marble authorized case

- [ ] Assess current public scene page and VR page for allowed asset discovery
- [ ] Establish reproducible, permission-respecting SPZ retrieval *if public/authorized*
- [ ] Verify SPZ header and actual splat count with a tested parser; record SHA-256
- [ ] Test supported Blender import/render with exact version and scene
- [ ] Investigate whether **legitimately available** mesh GLB/collider/texture variants exist
- [ ] If no mesh access, document reconstruction or manual-scene alternative; no entitlement bypass

**Acceptance:** source-to-asset provenance + format-specific validation + clearly labeled splat-vs-mesh outcome.

## M3 — Reliable cross-provider CLI and asset inspector

- [ ] Implement `src/download_without_export/` separation defined in Architecture
- [ ] JSON manifest schema and normalized statuses/exit codes
- [ ] Security checks: no local-file/localhost/unsafe redirects, URL scheme allowlist, secret redaction, size/time caps
- [ ] Real format parsers/import tests, not just magic bytes
- [ ] CLI documentation and tests across Windows/Linux/Colab

**Acceptance:** robust, least-privilege and repeatable on sanctioned assets.

## M4 — Blender editable scene pipeline

- [ ] Controlled GLB/FBX/OBJ import tests with textures/UV and independent-object measurements
- [ ] Compatible SPZ rendering test, if allowed and supported; version matrix
- [ ] Optional splat-to-mesh **experimental** path with loss/quality report
- [ ] Blender extraction/report script and asset manifests
- [ ] Rigged character + scene + 10-second 16:9 preview render

**Acceptance:** real Blender artifact showing what can/cannot be edited, not cosmetic format renaming.

## M5 — GPU notebook workflows and product polish

- [ ] Colab/Kaggle setup templates that probe GPU/Blender version instead of promising resources
- [ ] Reproducible sample scene and short MP4 smoke test
- [ ] Optional UI; batch jobs with queue/state, logs, retries and per-provider legal notices
- [ ] Backward-compatible machine-readable output, release notes, examples

## Good first issues

1. **Nuxt resolver test coverage**: synthetic indexed array with false-positive adjacent model and expired URL, no network.
2. **SPZ format inspector**: use an official/supported parser and an owner-created sample to report actual splat count.
3. **Blender import probe**: safe background script collecting mesh/armature/material stats; version pinning.
4. **Tripo CLI safety**: accept explicit ID, redact URLs, atomic streaming file validation and permission warnings.
5. **Colab smoke test**: no credentials; verify 1 frame render and attached authorized scene.

## Stop conditions

Do not pursue a purported download if doing so requires defeating access controls, stealing private assets, or violating permissions. Mark it as **blocked**; offer independently generated/authorized alternatives.
