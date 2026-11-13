# Troubleshooting and honest diagnostics

## Network and website errors

| Symptom | What is known | Correct next action |
|---|---|---|
| `curl: (6) Could not resolve host` | The environment could not resolve that hostname | Inspect DNS/proxy/network configuration; **do not** claim every website is unreachable |
| `curl: (56) CONNECT tunnel failed, response 403` | Outbound proxy denied an HTTPS tunnel **before** the provider page loaded | Obtain an **approved** allowlist/network-environment change; don't try to evade it |
| Provider returns HTTP `401` | Authentication may be required | Stop unless authorized credentials and permitted API flow exist |
| Provider returns HTTP `403` | Provider/access policy refused request | Respect denial; check permission/plan; do not circumvent |
| Provider returns HTTP `404` | Requested page/file missing, moved or intentionally hidden | Verify URL and current documentation; do not guess private endpoints |
| Provider returns HTTP `429` | Rate limit | Back off according to site policy; no proxy rotation/evading |
| HTML downloaded instead of 3D file | Redirect to a page, login or error; link expired or retrieval wrong | Inspect status/content-type, safely re-resolve if authorized; don't rename file to `.fbx` |
| Signed URL expired | Previously valid URL no longer works | Refresh legitimate public page metadata; preserve new URL privately |

Network failures are **environment/tool permissions**, not a benchmark comparing underlying AI models. A generated script without downloaded bytes is an intermediate artifact only.

## Tripo-specific

- **No `__NUXT_DATA__`:** page markup changed or requires interactive JS/auth. Record current HTML diagnostic metadata only; do not attempt security bypass.
- **Exact model missing:** never fall back to a similarly named, related or featured model.
- **Ambiguous matching URLs:** fail closed; investigate source ownership and matching IDs.
- **Filename extension guessed incorrectly:** `.fbx` fallback in the historical script is not proof of format. Compare bytes/signature and report failure clearly.
- **Blender optional check skipped:** do not claim import success; record `not_tested`.
- **Different host on redirect:** investigate whether authorized and permitted; do not silently add hosts or bypass network controls.
- **Missing textures:** FBX may reference external images that were never provided; mark incomplete rather than claiming a textured download.

## Marble-specific

- **SPZ works but no edit-able furniture:** expected, because splats do not inherently contain separable polygon geometry.
- **No available GLB:** do not fabricate a GLB direct URL. Provider may offer a distinct authorized mesh-export path.
- **Viewable in a browser but cannot download:** a viewer alone does not prove a file may legally be retrieved or that mesh/texture assets are exposed.
- **Blender import failure:** inspect Blender version and add-on; do not treat a successful unrelated Blender test as proof.

## Reporting template

```text
Target URL: [redacted public page only]
Target ID:
Environment (OS, Python, curl, Blender versions):
Authorization basis:
Page retrieval: VERIFIED / FAILED / NOT_TESTED
Exact-ID extraction: VERIFIED / FAILED / NOT_TESTED
Bytes saved: VERIFIED / FAILED / NOT_TESTED
Filename; bytes; SHA-256: [actual values only]
File type/header: VERIFIED / FAILED / NOT_TESTED
Blender import: VERIFIED / FAILED / NOT_TESTED
Mesh vs splat; object/rig/material counts: [measured only]
First blocked step:
Error (without signed URL, cookies or personal data):
Smallest authorized fix:
```
