# Serbia Gov Status

Community-run public status page for Serbian e-government services.

This project monitors the public availability of selected Serbian
e-government landing pages with low-rate Gatus probes. It is a community
project and is not affiliated with, endorsed by, or operated by any Serbian
government institution.

The MVP covers:

- eUprava
- eID.gov.rs
- Welcome to Serbia
- ePorezi
- APR
- LPA
- eKatastar
- data.gov.rs

Service details and URL choices are documented in `docs/services.md`.

## Local Startup

Start Gatus from the repository root:

```sh
docker compose up
```

The local status page is available at http://localhost:8080 by default.
Set `GATUS_PORT` to use another host port:

```sh
GATUS_PORT=8081 docker compose up
```

Validate the Compose file:

```sh
docker compose config
```

Stop the local container:

```sh
docker compose down
```

## Probe Policy

The probes must stay safe, public, and low-rate:

- Use public landing pages or public service entry points.
- Do not log in, submit forms, bypass CAPTCHA, access private data, or collect
  personal data.
- Do not probe authenticated account areas, inboxes, payment workflows,
  document-upload flows, or search results that expose private records.
- Keep the default interval conservative; the initial endpoints use `10m`.
- Use expected-text checks only for stable public text that is unlikely to
  change with localization, redirects, cookie banners, or dynamic content.

The full policy is in `docs/probe-policy.md`.

## Service Changes

To add, change, or remove a service:

1. Check that the URL fits `docs/probe-policy.md`.
2. Prefer a public landing page over a deep endpoint unless the deep endpoint is
   explicitly public, stable, and safe.
3. Add or update the endpoint in `config/config.yaml`.
4. Assign one of the existing groups: Identity, Core e-government, Immigration,
   Taxes, Business, Property, or Open data.
5. Add HTTP status, latency, and HTTPS certificate expiry conditions where
   supported.
6. Add an expected-text condition only when the text is stable and public.
7. Update `docs/services.md` with the URL, group, URL type, and rationale.
8. Run validation:

```sh
python -m unittest discover
docker compose config
```

## Planned Maintenance

The ePorezi electronic services are publicly documented as available from
06:00 to midnight, and the public maintenance page shows regular daily system
maintenance from 00:00 to 06:00.

The ePorezi endpoint is configured with a per-endpoint Gatus maintenance window
from 00:00 to 06:00 in `Europe/Belgrade`. Expected ePorezi unavailability
during that window should not be treated as a community outage incident.

References:

- https://www.purs.gov.rs/en/E-taxes/Information.html
- https://eporezi.purs.gov.rs/error/maintenance.htm

## Telegram Alerts

Telegram alerts are disabled by default so the project can start without local
secrets.

Copy the example environment file and fill in local values:

```sh
cp .env.example .env
```

Set these variables in `.env`:

```env
TELEGRAM_ALERTS_ENABLED=true
TELEGRAM_BOT_TOKEN=replace-with-your-telegram-bot-token
TELEGRAM_CHAT_ID=replace-with-your-telegram-chat-id
```

`TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are passed to Gatus through Docker
Compose and substituted into `config/config.yaml` at runtime. Keep real values
only in `.env`; this file is ignored by Git.

After updating `.env`, validate and start:

```sh
docker compose config
docker compose up
```

Test alerting with a private local chat or test channel first. Do not commit a
real bot token, chat ID, generated database, or local `.env` file.
