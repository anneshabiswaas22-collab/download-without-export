# Architecture and implementation plan

The project is **provider-adapter + independent asset validation + optional Blender processing**, not a monolithic scraper.

```text
Authorized public/owner-controlled URL
               |
        Provider identification
               |
        Access/rights preflight
               |
      Provider-specific resolver
  (exact ID, public page metadata)
               |
       Authorized file transport
 (preserve signed query, redirect policy)
               |
      Temporary download + checks
 (bytes, signature, hash, type, errors)
               |
       Validated asset + report
              / \
      Blender import  Archive metadata
        /       \
  Splat rendering  Polygon mesh editing
                        |
                 Texture/rig/scene tests
                        |
                Preview render (optional)
```

## Present implementation

- `scripts/tripo/download_tripo_model.py` — recovered Tripo3D **single-model** Nuxt page resolver / curl downloader / header check / optional FBX import. A legacy script with hardcoded study-case ID; *not* a general provider API or a currently verified end-to-end run.
- `scripts/inspect_asset.py` — offline inspector of locally obtained files: size, streaming SHA-256, basic recognizable file headers. It is **not** a geometry parser or downloader.
- `tests/` — no-network unit tests.
- `docs/` — project decisions, evidence, handoff and research.

## Intended package boundaries (proposed, not yet implemented)

```text
src/download_without_export/
  cli.py                 # argument parsing, CLI output, stable exit codes
  providers/base.py      # resolve(url)->candidate(s), supported types
  providers/tripo.py     # Nuxt exact-ID resolver
  providers/marble.py    # public data only, return NOT_AVAILABLE if unsupported
  transport.py           # controlled curl/requests transport
  validate.py            # magic bytes, type parsing, SHA-256
  report.py              # JSON evidence manifest
  blender.py             # optional subprocess import/probe
tests/fixtures/          # small synthetic, rights-cleared fixtures
```

Do not claim the proposed tree already exists.

## Provider adapter contract

Every adapter must:
1. Match allowed and expected provider hosts (avoid arbitrary URL execution); use exact model/world IDs supplied by caller.
2. Produce *candidate* metadata with original source URL, observed timestamp, representation and public evidence; never fabricate a mesh link.
3. Reject ambiguous IDs or mixed related-item matches.
4. Return a structured status: `PUBLIC_FILE_AVAILABLE`, `NO_PUBLIC_ASSET`, `LOGIN_REQUIRED`, `ENTITLEMENT_REQUIRED`, `NETWORK_BLOCKED`, `SOURCE_CHANGED`, `INVALID_SOURCE`.
5. Treat signed URLs as secrets (redact query string, do not commit/relog); reject non-HTTPS and unsafe hosts by default unless a documented trusted exception applies.
6. Follow redirects only to authorized destinations. Never attempt to evade a 401, 403, gated export or protective control.

## Validation and verification layers

| Layer | Check | Meaning |
|---|---|---|
| L0 | Network, curl HTTP status and host | Did an authorized request reach its target? |
| L1 | Bytes written, size > 0 and digest | Something downloaded and is stable |
| L2 | Header/format signature + no HTML/login page | Plausible actual asset |
| L3 | Structural parser (GLB JSON/BIN, FBX objects, PLY, SPZ reader) | Geometry/container integrity, implementation pending |
| L4 | Blender import, vertex/object/material/texture counts | Real usable scene |
| L5 | Sample scene render; screenshot comparison | Visual acceptance |
| L6 | Rig/body motion and MP4 render | Animation acceptance |

Tests must name their achieved layer, not simply state `success`.

## Suggested manifest (`docs/schemas/asset_manifest.example.json` is illustrative)

```json
{
  "schema_version": 1,
  "provider": "tripo",
  "source_page": "https://studio.tripo3d.ai/3d-model/EXAMPLE",
  "source_id": "EXAMPLE",
  "permission_basis": "owner-approved public access (document exact basis)",
  "fetched_at_utc": "example timestamp",
  "output_filename": "example.glb",
  "size_bytes": 12345,
  "sha256": "<verified digest>",
  "representation": "polygon_mesh",
  "signature_check": "passed",
  "blender_import": "not_tested",
  "notes": "This is example data; never use as actual evidence."
}
```

## Key engineering risks

- **Nuxt/devalue encoding drift:** schemas or indexed references can change without warning; add versioned fixtures.
- **Download URLs:** short-lived signatures; avoid caching or leaking signed query params; if expired, re-resolve through permitted page.
- **Access policy:** DNS failure or proxy 403 happens before provider access decisions; diagnose separately.
- **SPZ vs mesh:** a visual world representation cannot guarantee editable objects. Geometry reconstruction may lose details.
- **Output licensing:** do not assume publicly viewable means legally downloadable or distributable.
- **3D file security:** do not automatically execute scripts embedded in projects, untrusted archives or Blender files; prefer isolated processing of unknown assets.

## Definition of done for PRs

Reproducible steps, tests/fixtures, provider source evidence, permission reasoning, failure-mode coverage, no credential exposure, and current-vs-historical verification clearly separated.
