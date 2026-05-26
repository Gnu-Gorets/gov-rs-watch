# Operational Runbook

This runbook covers local operation for the community-run Serbia Gov Status
MVP. It assumes commands are run from the repository root.

## Local Startup

Validate the Compose file before starting:

```sh
docker compose config
```

Start Gatus:

```sh
docker compose up
```

The status page is available at http://localhost:8080 by default. To use a
different host port, set `GATUS_PORT`:

```sh
GATUS_PORT=8081 docker compose up
```

Stop Gatus:

```sh
docker compose down
```

Use `docker compose down -v` only when the local SQLite history in the
`gatus-data` volume should be removed.

## Config Validation

Run both repository-level tests and Compose validation after changing endpoint
configuration or documentation:

```sh
python -m unittest discover
docker compose config
```

`docker compose config` checks Compose syntax, environment variable
substitution, mounted files, and the effective service definition. It does not
prove that every remote service is healthy.

## Service Changes

To add, change, or remove a service:

1. Confirm the URL fits `docs/probe-policy.md`.
2. Prefer a public landing page or public entry point over a deep application
   URL.
3. Reject URLs that require login, form submission, CAPTCHA bypass, session
   state, private data, or high-frequency probing.
4. Update `config/config.yaml`.
5. Assign one of the existing groups: Identity, Core e-government, Immigration,
   Taxes, Business, Property, or Open data.
6. Include HTTP success, practical latency, and HTTPS certificate expiry checks
   where supported by Gatus.
7. Add expected-text checks only for stable public text.
8. Update `docs/services.md` with the service name, URL, group, URL type, and
   probe rationale.
9. Run the validation commands from this runbook.

When removing a service, also remove related documentation and any stale test
expectations.

## False Positives

When an endpoint reports a failure:

1. Check whether the failure happened inside a configured maintenance window.
2. Compare the failed condition with the current service behavior.
3. Open the public URL manually without logging in or submitting forms.
4. Check for redirects, localization changes, cookie banners, or redesigned
   page content before treating a text assertion as a real outage.
5. Confirm whether only one endpoint is failing or a broader network/DNS/TLS
   issue is affecting several endpoints.
6. If the service is reachable but the check is fragile, adjust or remove the
   fragile assertion and update `docs/services.md`.

Do not use private accounts, authenticated pages, document-upload workflows, or
taxpayer data while investigating.

## Planned Maintenance And Noisy Endpoints

The ePorezi endpoint has a configured maintenance window from 00:00 to 06:00 in
`Europe/Belgrade`. Expected ePorezi unavailability during that window should
not be treated as a community outage incident.

For noisy endpoints:

1. Prefer relaxing or removing fragile expected-text checks before changing the
   probe target.
2. Keep the interval conservative unless there is a clear operational reason.
3. Document recurring maintenance or known noisy behavior in `docs/services.md`
   and this runbook.
4. Do not move probes into authenticated or stateful application flows to avoid
   noise.

## Telegram Alert Test

Telegram alerts are disabled by default. Test them only with a private local
chat or test channel.

Create a local `.env` from the example and fill in test-only values:

```sh
cp .env.example .env
```

Set:

```env
TELEGRAM_ALERTS_ENABLED=true
TELEGRAM_BOT_TOKEN=replace-with-test-bot-token
TELEGRAM_CHAT_ID=replace-with-test-chat-id
```

Validate and start Gatus:

```sh
docker compose config
docker compose up
```

To trigger an alert safely during local testing, temporarily point a local test
copy of an endpoint at a guaranteed-failing local URL, confirm the alert reaches
the test chat, then revert the change before committing. Never commit real bot
tokens, real chat IDs, `.env`, generated databases, or local runtime data.
