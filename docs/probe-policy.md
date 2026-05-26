# Probe Policy

This project checks public availability only. Probes must be safe for the
target service, useful for a public status page, and respectful of public
infrastructure.

## Scope

Allowed targets:

- Public landing pages.
- Public service entry points.
- Public informational pages that do not require a session.
- Public open-data portals or catalog pages.

Forbidden targets and behavior:

- Do not log in.
- Do not submit forms.
- Do not bypass CAPTCHA.
- Do not access private data.
- Do not collect personal data.
- Do not probe authenticated account pages, tax inboxes, payment flows,
  document-upload flows, or registration flows.
- Do not probe URLs that require session state, cookies from a login flow, or a
  user-specific token.
- Do not use high-frequency probing.

## Choosing URLs

Prefer the safest public URL that still indicates service availability. In most
cases this is a landing page or public entry point, not a deep application URL.

A URL is a good candidate when:

- It is reachable without login.
- It does not require form input.
- It does not expose private records.
- It has a stable public purpose.
- It can be checked at a low rate without creating load.
- It is clearly related to Serbian e-government or public-service
  availability.

Reject a URL when the probe would enter an application workflow, trigger
security controls, expose user-specific content, or create noise for the
service operator.

## Assertions

Each endpoint should validate:

- HTTP success status.
- Practical response latency.
- TLS certificate expiry for HTTPS endpoints where Gatus supports it.

Expected-text checks are optional. Use them only for stable public text that is
unlikely to fail because of:

- Localization changes.
- Redirects.
- Cookie banners.
- Dynamic content.
- Rotating notices or news.
- A/B tests or redesigned page chrome.

Remove a text check if it creates false positives or depends on fragile page
content.

## Frequency

Keep checks low-rate. The initial MVP uses a `10m` interval for public pages.
Do not reduce intervals unless there is a clear operational reason and the
target remains safe to probe.

## Affiliation

This is a community-run project. Documentation, UI text, issue comments, and
release notes must not imply official government affiliation, endorsement, or
operation.
