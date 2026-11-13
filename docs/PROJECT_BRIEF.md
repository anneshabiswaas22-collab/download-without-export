# Project brief: Download Without Export

**Project phase:** research → reliable, repeatable implementation. **Owner's main outcome:** an actual, verified 3D asset file, preferably a textured, editable Blender mesh, for a user-authorized public model/world link.

## Background and scope

Two concrete cases drove this project:
- [World Labs Marble scene](https://marble.worldlabs.ai/world/608d6222-8bb9-4575-8845-b1efd2f980ab) and its [VR page](https://marble.worldlabs.ai/worldvr/608d6222-8bb9-4575-8845-b1efd2f980ab); both reference the same world ID.
- [Tripo3D model](https://studio.tripo3d.ai/3d-model/e3bca070-3984-4aa3-8d54-1192acc9da1e).

The requester prefers direct retrieval of already accessible files **without clicking a site's Export button**, wants formats beyond `.spz`, wants Blender-editable geometry/materials, and has explored free/free-tier 3D generators (Meshy, Tripo, Marble, KIRI Engine, open source) and optional animated character/background rendering on Colab/Kaggle GPUs.

## User stories

1. As an artist, I provide a public, authorized page URL and receive the actual model/world file with checksums, byte size, type, source and reproducible retrieval steps.
2. As an artist, I want the script to tell me when the asset is **only a Gaussian splat** and not pretend that renaming or converting the container makes it an editable polygon mesh.
3. As a model creator, I want the best *permitted* mesh format that is genuinely available from the source—not a promised `.glb` that the public page does not expose.
4. As a developer, I need to distinguish website changes, provider denial, expired signed URLs, proxy policy, DNS failure, malformed content, corrupted data, and Blender incompatibility.
5. As an animator, I want a practical pipeline from texture/mesh/rig data to a saved `.blend` scene and eventually animated MP4, with a staged 10-second preview.
6. As a contributor, I want documentation, tests and issues to begin contributing without original conversation access.

## Functional requirements

- Input: explicit page URL and/or provider-specific ID.
- Preflight: allowed network endpoints and legitimate download rights; use approved environment configurations.
- Resolve: parse only documented/publicly accessible page data; select the **exact ID**; never confuse related or recommended items.
- Retrieve: preserve the full existing signed URL; obey expiration, HTTP status, provider terms and rate limits.
- Validate: not HTML/error page; byte count and SHA-256; format-specific header; optional geometry parsing and Blender import.
- Publish an honest outcome report: `VERIFIED`, `FAILED`, `NOT_TESTED` at each stage, with no invented success metrics.
- Preserve separation between download/retrieval, format conversion, scene reconstruction, rigging and rendering.

## Non-goals / prohibitions

- No bypass of paid Export gates, authentication, DRM, API security, quotas, network rules or contractual restrictions.
- No harvesting private objects or copyrighted third-party asset binaries for redistribution.
- No guarantee that a 360 scene or single image provides perfect, isolated 3D furniture, invisible back surfaces, human rigs or physically accurate texture/material maps.
- No claim that a downloader script itself is an asset download.
- No storage of cookies, access tokens, signed URLs or personally identifying logs in the public repo.

## Acceptance criteria

**A reproducible source-to-file case is complete only when:** the source and permission basis are recorded; the exact asset is unambiguously selected; actual bytes saved; file hash, size and header checked; its representation reported accurately; Blender testing recorded as passed/failed/skipped; log scrubbed; no bypass employed.

**A Blender-editable-scene case is complete only when:** actual polygon mesh(es) are importable/editable; materials/textures inspected; separate semantic objects/rigging documented (or explicitly absent); editable project output preserved if redistribution is permitted.

**An animation case is complete only when:** specified character + environment are available, rig compatibility checked, a short end-to-end render is verified before scaling to longer/high-resolution outputs.

## Value proposition and audience

Creators building virtual environments, educational/animated films, image-to-3D pipelines and developer-friendly automation. Priority order: **correct representation → trustworthy verification → legitimate access → reproducibility → automation → Blender animation**.
