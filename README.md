# Download Without Export

**A reproducible, permission-respecting research and tooling project for retrieving accessible 3D assets from public model/world pages and making those assets useful in Blender.**

> **Status (13 November 2026):** Repository initialized from prior project discussions and recovered project files. A Tripo page downloader and research report are included. **No live network download, current vendor permissions, or Blender import was verified in this repository initialization.** Historical results are explicitly marked in [the evidence log](docs/EVIDENCE_LOG.md).

## Mission

Make it easier to obtain the **actual 3D file**, not just a screenshot, a prompt, or a browser viewer, when an owner-authorized/public page already makes the asset available for direct retrieval *without clicking the site's Export button*. Then validate the bytes, identify their real 3D representation and prepare a practical path toward Blender editing, animation, and rendering.

The project serves artists, developers, AI-assisted 3D creators and GPU-notebook users who need repeatable, verifiable results. **"No Export click" is a workflow constraint, not permission to evade paywalls, authentication, licenses, DRM, technical access restrictions or service policies.** Do not attempt to unlock an export-only asset by defeating controls. If a permissible download is not exposed, report it and use an authorized export or alternate creation workflow.

## Exact study cases

| Case | Public page | Desired output | Recorded outcome |
|---|---|---|---|
| **World Labs Marble** | [World view](https://marble.worldlabs.ai/world/608d6222-8bb9-4575-8845-b1efd2f980ab) / [VR view](https://marble.worldlabs.ai/worldvr/608d6222-8bb9-4575-8845-b1efd2f980ab) | Actual world asset; ideally editable textured scene | An earlier session reported a ~30 MB, ~1.92M-splat **SPZ** download and a converted Blender project. A splat is **not** an editable polygon mesh. Binary files have **not** been recovered into this repo. |
| **Tripo3D** | [Model page](https://studio.tripo3d.ai/3d-model/e3bca070-3984-4aa3-8d54-1192acc9da1e) | Actual model file, preferably FBX/GLB with textures | An earlier session reported **Taj_Mahal.fbx** downloaded and Blender checked. Other environments reported network proxy/DNS failures. The historical binary is **not included**; a downloader script exists. |

All evidence and limitations: [docs/EVIDENCE_LOG.md](docs/EVIDENCE_LOG.md).

## What this project is — and is not

- **Is:** a collection of tested/research-derived methods, validated downloads when accessible, reusable scripts, failure diagnosis, 3D file inspection, Blender guidance and documented provider-specific adapters.
- **Is not:** a universal "download anything" extractor, a payment/access-control bypass, a guarantee that a splat can be turned into individually editable furniture, or a claim that current vendor pages still expose the same public asset links.
- **Key principle:** a successful HTTP response is not a successful asset download. Validate file signatures, size, geometry/representation and—when practical—an actual Blender import.

## Start here

**New developer:** Read [Project brief](docs/PROJECT_BRIEF.md) → [Architecture](docs/ARCHITECTURE.md) → [Evidence log](docs/EVIDENCE_LOG.md) → [Roadmap](docs/ROADMAP.md) → [Contributing](CONTRIBUTING.md).

**Run the recovered Tripo downloader (only for assets you are authorized to download):**

```bash
python --version
curl --version
python scripts/tripo/download_tripo_model.py
```

The legacy Tripo downloader supports Python 3.8+ and curl on PATH. The offline inspector and test suite require **Python 3.10+**. It fetches fresh page data, seeks an **exact-ID** model URL in Nuxt data, follows the existing URL including signed parameters, validates downloaded headers and optionally tests FBX in Blender. **It may fail if the website changes, the file is not publicly available, or the execution environment cannot reach it.** The script is carried over from a previously generated artifact and is not a currently verified live integration.

**Offline metadata check of an asset you legally obtained:**

```bash
python scripts/inspect_asset.py /path/to/asset.glb
python -m unittest discover -s tests -v
```

No project assets need to be uploaded to use these checks.

## Blender representation warning

| Format/type | Good for | Not guaranteed |
|---|---|---|
| **SPZ / PLY Gaussian splats** | Immersive views and background rendering with compatible tools | Mesh Edit Mode, independently moving objects, UV-editable materials |
| **GLB / glTF / FBX / OBJ polygon meshes** | Mesh editing, textures, scene assembly; potentially armatures | Clean retopology, separate furniture, working body/facial rig |
| **.blend** | Blender project container | That underlying objects are polygons instead of splats |

For the distinction between **appearance**, **mesh**, **texture**, **rig** and **animation**, see [Asset formats](docs/ASSET_FORMATS.md) and [Blender workflows](docs/BLENDER_WORKFLOWS.md).

## Repository layout

```text
README.md
CONTRIBUTING.md
SECURITY.md
LICENSE
docs/
  PROJECT_BRIEF.md
  ARCHITECTURE.md
  EVIDENCE_LOG.md
  PROVIDERS.md
  ASSET_FORMATS.md
  BLENDER_WORKFLOWS.md
  TROUBLESHOOTING.md
  ROADMAP.md
  DECISIONS.md
  RESEARCH_REPORT.md
scripts/
  tripo/download_tripo_model.py
  inspect_asset.py
tests/
  test_inspect_asset.py
  test_tripo_parser.py
.github/
  ISSUE_TEMPLATE/
    bug_report.md
    provider_request.md
  workflows/tests.yml
.gitignore
```

## Definition of a successful case

An accepted case documents: **source URL, permission/rights basis, timestamp, actual HTTP and file retrieval steps, final output path, bytes and SHA-256, signature and parsed type, Blender import/visual test (or clearly "not tested"), and any blockers.** No credentials, expiring signed URLs, cookies or private data in logs/commits.

## Original user goals preserved

1. Download accessible public Marble/Tripo assets **without pressing Export** when permitted.
2. Obtain **other real file formats, not only SPZ**, if genuinely available.
3. Produce **textured, editable Blender geometry**, not merely a rendered 3D appearance.
4. Explore character/full-body-image → 3D rig/animation and environment-image → 3D scene pipelines with **free/free-tier options preferred**.
5. Support repeatable CPU/cloud/Colab/Kaggle-compatible workflows where practical, with measurable results.
6. Make each outcome independently understandable to developers who were **not present in the original chat**.

See [Research report](docs/RESEARCH_REPORT.md) for the recovered in-depth tool comparison. Treat prices, free tiers and model-version details in that **8 November 2026** report as time-sensitive.

## Progress and contribution

Current engineering status, missing assets and next milestones are in [Roadmap](docs/ROADMAP.md). Open an issue or PR with reproducible evidence and tests. See [Contributing](CONTRIBUTING.md) before adding provider integrations.

## Legal and operational boundaries

Download only content you own, are licensed to download or are otherwise explicitly authorized to retrieve. Respect terms, copyright, network access policies, consent, privacy and rate limits. Do not bypass logins, payment gates, export entitlements, API restrictions, signed-link authorization, traffic controls or DRM. Do not publish someone else's 3D content without redistribution rights.

**The repository documents a workflow; it does not grant rights to any third-party asset or service.**
