# Security policy

This project interacts with external URLs and untrusted 3D files. Contributors must not add extraction techniques that evade authentication, entitlements, anti-bot controls, DRM, network/proxy restrictions or provider terms.

## Reporting security issues

Do **not** publish exploit steps, credentials or sensitive endpoints in public issues. Contact the repository maintainer through an appropriate private GitHub contact channel if available.

## Mandatory controls for new providers

- Allowlist provider origin hosts and validate redirect hosts; no automatic request to arbitrary supplied private IP, localhost, metadata services or non-HTTP(S) schemes.
- Use HTTPS by default; never disable TLS checks just to complete a task.
- Bound download size, redirects and timeouts; handle partial files and atomic rename.
- Redact credentials, cookies, signed query parameters and auth headers in logs.
- Do not check in copyrighted assets without redistribution authorization.
- Do not unpickle, execute scripts or run untrusted add-ons from downloaded assets.
- Import unknown 3D files only with trusted Blender plugins and preferably isolated workers; never promise all .blend files are safe.
- Keep authorizations human-approved and narrowly scoped; make integration tests opt-in.

The recovered original Tripo script predates these planned hardening controls and is presented as a **legacy proof of concept**, not a hardened server-side downloader.
