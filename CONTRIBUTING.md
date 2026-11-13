# Contributing

We welcome focused documentation, test, Blender pipeline and provider-integration contributions.

## Getting started

1. Read `README.md`, `docs/PROJECT_BRIEF.md`, `docs/EVIDENCE_LOG.md`, and `docs/ROADMAP.md`.
2. Use **Python 3.10+** for the offline inspector and test suite; the legacy downloader itself was written for Python 3.8+. Use a current curl and install Blender only for optional integration tests.
3. Run `python -m unittest discover -s tests -v`.
4. Pick a roadmap task, create a feature branch and submit a PR against `main`.
5. Include real and synthetic test evidence, references and a summary of remaining unknowns.

## PR checklist

- [ ] I can state the legal/permission basis for any retrieved content and provider endpoints.
- [ ] No DRM, login, quota, export entitlement, paywall, allowlist or access-control bypass.
- [ ] No credentials, session cookies, private metadata, signed URLs or unauthorized asset binaries committed.
- [ ] Exact-ID matching works; no unrelated recommended model.
- [ ] Failure paths (network, HTTP, metadata change, expired URL, invalid bytes) are tested.
- [ ] Reports distinguish actual tests from assumptions and prior-session claims.
- [ ] I identified splat vs mesh, editable objects vs fused geometry, textures vs rig separately.
- [ ] I documented platform requirements; CI unit tests pass.

## Testing discipline

Use tiny, author-created fixtures or public-domain/openly redistributable examples with license attribution. Avoid live vendor access during unit tests. Integration tests must be opt-in, with explicit rights and network requirements. `VALID_HEADER` does **not** equal Blender-editable mesh or verified geometry. No invented benchmark numbers.

## Contributor code standards

Prefer dependency-light, type-annotated Python with small testable modules; no unsafe file paths or auto-execution of unknown 3D assets. Validate URLs before making network requests. Sanitize errors and debug logs, particularly signed query strings and secrets. Favor deterministic tests and explicit statuses over generic success labels.

## Reporting bugs

Use the issue templates. Include provider, exact public-page URL (without expiring tokens), environment, observed/expected behavior, repro steps and redacted logs. Do not upload copyrighted model files without redistribution rights.

## License and third-party content

The repository's own code/documentation license does **not** confer licenses to Tripo, Marble, uploaded models, trademarks, third-party research or linked software. Respect their individual license terms.
