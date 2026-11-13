# New developer / Codex handoff

You are joining **Download Without Export**. You do not need the chat history.

**Read in order:** `README.md` → `docs/PROJECT_BRIEF.md` → `docs/ARCHITECTURE.md` → `docs/EVIDENCE_LOG.md` → `docs/ROADMAP.md` → `CONTRIBUTING.md`.

## Hard constraints

- Only retrieve files already public and **authorized** to obtain; no paywall, export entitlement, authentication, DRM, proxy or network-policy bypass.
- Output must be the **actual asset bytes**, not merely code or a screenshot, to claim download success.
- Differentiate **SPZ splats**, **poly meshes**, **semantic object hierarchy**, **textures**, **rigging** and **renderable Blender projects**.
- Do not claim the exact resort world imports in Blender 5.3: historical notes conflict; verify it.
- Do not claim previous Taj Mahal FBX or resort SPZ binaries are in the repository; they're not.
- Expose precise error stages and redact all signed/private URL query strings.
- Use cheap/free tooling first where it produces truthful results; do not invent free-tier details.
- For AI/agent contributors: write code + tests, then report evidence; do not fabricate execution results.

## Known target identifiers

**Tripo:** `e3bca070-3984-4aa3-8d54-1192acc9da1e` (historical FBX `Taj_Mahal.fbx`).  
**Marble:** `608d6222-8bb9-4575-8845-b1efd2f980ab` (two views of one world; historical 30 MB 1.92M-splat SPZ).

## Current code to start with

```bash
python -m unittest discover -s tests -v
python scripts/inspect_asset.py --help
python scripts/tripo/download_tripo_model.py  # only if authorized and network enabled
```

You can implement milestone **M1** immediately by improving parsing, CLI error semantics and tests **offline** before requesting network credentials/permissions. Another good task is a verified **M2** format-only SPZ parser using a small rights-cleared fixture.

## PR output expectations

Explain *what changed*, *what was actually run*, *how to reproduce*, *which rights/hosts are involved*, *what remains untested*, and *whether any output is splat/mesh/rig/render*.

Historical research lives in `docs/RESEARCH_REPORT.md` (dated Nov 8, 2026); current details must be rechecked against primary-source docs before implementing feature/paywall assumptions.
