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
