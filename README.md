# Serbia Gov Status

Community-run public status page for Serbian e-government services.

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
