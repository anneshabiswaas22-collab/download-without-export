# Providers and workflows

## Tripo3D — exact-ID public-page case

**Target:** `e3bca070-3984-4aa3-8d54-1192acc9da1e` ([page](https://studio.tripo3d.ai/3d-model/e3bca070-3984-4aa3-8d54-1192acc9da1e)).

Existing recovered script: `python scripts/tripo/download_tripo_model.py`.

1. Verify you have a legitimate right to retrieve the public asset and an approved network connection.
2. Fetch the live public page with normal curl/proxy settings, not a security bypass.
3. Parse `<script id="__NUXT_DATA__">` into an indexed data array.
4. Resolve the Nuxt reference indices; **find only** the record whose `id` or `itemId` exactly matches the requested model.
5. Read `model_url`, `modelUrl`, or the nested `model.modelUrl` on that exact record. Never pick the first nearby URL or a related item.
6. When the link is legitimately public and downloadable, use the exact URL including its short-lived signed parameters with `curl -fL`. **Do not print or commit signed parameters.** Do not try to change or forge signatures.
7. Verify bytes, header and Blender import. If no public downloadable URL exists, **stop** and report this accurately; do not work around entitlements.

These steps are **historical working assumptions** and subject to Nuxt/site changes. The original script is narrowly scoped to one model. If the provider requires credentials, paid export or disabled downloads, do not build a bypass.

## World Labs Marble — world and worldvr views

**Target:** `608d6222-8bb9-4575-8845-b1efd2f980ab`.
- [3D world page](https://marble.worldlabs.ai/world/608d6222-8bb9-4575-8845-b1efd2f980ab)
- [VR view](https://marble.worldlabs.ai/worldvr/608d6222-8bb9-4575-8845-b1efd2f980ab)

A historical attempt reported an SPZ full-resolution resort world (~30 MB, ~1.92M splats) retrieved without an Export-button interaction. **There is no saved reproducible SPZ resolver, download URL, checksum or binary in this repository.** This is an open task, not an existing adapter.

Investigate only public and permitted page metadata or exposed file resources. If only an authorized Export flow exposes a high-quality mesh, do **not** attempt to bypass the entitlement to obtain it. Use the allowed workflow instead or recreate geometry separately.

### Representations

- **SPZ/PLY splats:** visual/scene-view representations; not inherently UV-mapped, individually editable polygon furniture.
- **Collider GLB:** physics/navigation proxy mesh; not necessarily a high-quality renderable set.
- **HQ textured or vertex-color GLB:** possible polygon representation **if actually available under the provider plan and rights**, likely imperfect geometry with holes/fused objects.

Source pointers for verification: [Marble mesh docs](https://docs.worldlabs.ai/marble/export/mesh), [Gaussian splat docs](https://docs.worldlabs.ai/marble/export/gaussian-splat), [export specs](https://docs.worldlabs.ai/marble/export/specs). Confirm current policies/availability before claiming any feature is free or enabled.

## Image → 3D options explored

| Use case | Candidate | Strength | Verify before committing |
|---|---|---|---|
| Full-body character image | [Meshy](https://www.meshy.ai/), [Tripo](https://www.tripo3d.ai/) | Image → mesh; hosted rigging/animation options | Face/hand fidelity, skinning/rig, exports, commercial rights, current free tier |
| Open-source single-image object | [TripoSR](https://github.com/VAST-AI-Research/TripoSR), [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | Local/Colab experiments | VRAM, weights/license, topology, texture outputs |
| Imagined single-image world | [Marble](https://marble.worldlabs.ai/), [Hyper3D WorldGen](https://hyper3d.ai/features/worldgen) | Appearance and possible scene exports | Separate objects vs merged scene; format, cost, access |
| Real-world room/street | [KIRI Engine](https://www.kiriengine.app/), [Meshroom](https://alicevision.org/) | Multiview photogrammetry | Capture quality, free usage, correct scale and cleanup |
| Character motion | [Mixamo](https://www.mixamo.com/), own Blender rigs | Animation reuse/retarget | Current usage rights, compatible bones, facial animation |

The full dated comparison, strengths, limitations, links and references is preserved in [RESEARCH_REPORT.md](RESEARCH_REPORT.md). These are **options**, not proof of currently free exports or hands-on superiority.

## Provider discovery checklist

Record provider + version/date, known domains, robots/terms/access constraints, public page markup and permission basis, output types, signature/redirect patterns, error semantics, exact-ID matching fixtures, and a non-sensitive example manifest. Prefer official API/documentation when available and authorized.
