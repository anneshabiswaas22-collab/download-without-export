# Historical evidence log

**Purpose:** preserve project experience without confusing reported accomplishments with artifacts accessible in this repository. Compiled **13 November 2026** from available prior conversation context and project files; not a fresh end-to-end verification.

## Case A — Marble resort world

- World ID: `608d6222-8bb9-4575-8845-b1efd2f980ab`.
- Views: [world](https://marble.worldlabs.ai/world/608d6222-8bb9-4575-8845-b1efd2f980ab) and [worldvr](https://marble.worldlabs.ai/worldvr/608d6222-8bb9-4575-8845-b1efd2f980ab); historically recorded as the **same world**.
- Earlier response reported file names `Futuristic_Tropical_Ocean_Cliff_Resort.spz` / `Futuristic_Tropical_Ocean_Cliff_Resort_full_res.spz`, about **30 MB** and **1,920,000 Gaussian splats**, checksum/integrity claimed verified.
- Another prior summary refers to a converted approximately **55.5 MB** `.blend` and a Blender render.
- **Important evidence conflict:** a saved transcript explicitly states that **this exact SPZ was NOT tested for Blender 5.3 import** and a later note referred to a Blender **4.3.2** environment requiring compatible support. Do not promote general Blender support, an unrelated successful render, or a purported conversion to a **verified native import for this scene**.
- Representation: **Gaussian splats**, not polygon mesh or individual, independent props. A `.blend` containing splats does not make them independently editable sofas/walls.
- **Status in this repo:** historical report only; **SPZ and .blend binaries not present**. Original download URL, SHA-256 and current public asset availability are not recovered; cannot reproduce the exact download without inspecting the live public page again under authorized access.

## Case B — Tripo Taj Mahal model

- Exact target: [Tripo model](https://studio.tripo3d.ai/3d-model/e3bca070-3984-4aa3-8d54-1192acc9da1e).
- Prior session reported downloading `Taj_Mahal.fbx` and checking Blender import; the **binary is not present in this repo**. No hash, byte count, geometry count or current signed URL is retained here.
- Recoverable script: `scripts/tripo/download_tripo_model.py`, parses fresh page `__NUXT_DATA__` indexed array, resolves the exact model ID, reads `model_url` or `model.modelUrl`, downloads with curl, performs basic header check and optionally Blender verification.
- Another execution environment recorded `curl: (56) CONNECT tunnel failed, response 403` at the outbound proxy before Tripo HTML was fetched.
- Another execution environment recorded `curl: (6) Could not resolve host: studio.tripo3d.ai` and generated only a script, **not** a model file.
- Historically used hosts: `studio.tripo3d.ai` (page), `tripo-data.rg1.data.tripo3d.com` (FBX CDN). These observations are *not* a promise of current endpoints.
- **Current status:** script recovered; live site download / Blender check from this repo **not yet performed**. Distinct outcomes reflect environment capabilities, **not necessarily different model intelligence**.

## Evidence quality table

| Claim | Evidence available now | Status |
|---|---|---|
| Two Marble URLs point to the same world | Same world ID; prior transcript | Historical, reasonable |
| Marble SPZ was ~30MB / 1.92M splats | Prior response recorded; binary absent | Reported only |
| This exact Marble SPZ imports in Blender 5.3 | Contradictory earlier transcript; no file here | **Not verified** |
| Marble SPZ is directly editable polygon geometry | No; it is a splat representation | False |
| Tripo Taj Mahal FBX download succeeded somewhere | Historical user-reported conversation output; binary absent | Reported only |
| Tripo downloader handles a fixed study-case ID | Original Python script recovered | Source present; live integration not verified |
| Some cloud sessions were blocked by proxy or DNS | Exact error text in recovered notes | Historical error evidence |
| Repo currently contains signed model URLs | No; deliberately omitted | Not present |

## New test evidence template

When repeating any case, add an issue/PR note with:
- UTC date; environment; source page; exact item ID; provider rights or permission basis.
- Exit status and **redacted** HTTP response + response content type.
- File path, actual byte size, SHA-256, signature/magic check and parser result.
- Blender version, import path, mesh/splat count, texture/material count and optional visual render.
- If failed: failed step, exact error, whether the error originated at DNS, proxy, TLS, application HTTP, signing, parsing or geometry import.
- Do **not** put private filenames, personal information, access tokens, cookies or signed URL query strings in issues or commits.
