# CMS Admin

Simple django admin site for the cms golang project.

## Before you start

Make sure you point it to a prepopulated db and that the db has a schema called `admin`.

## Running

Using docker compose:
```bash
docker compose up --watch
```

## Inspecting models

```bash
./run.sh uv run manage.py inspectdb --database=cms > cms/models_new.py
```

Copy the new stuff into `cms/models.py` and update the admin.py file. Be sure to check the new models for any errors.

## Python packages

See the [docs](https://docs.astral.sh/uv/) for more information.

install:
```bash
./run.sh uv add <package==1.0.0>
```

remove:
```bash
./run.sh uv remove <package>
```

## Auto code linting

```bash
./run.sh uv run ruff format .
```

```bash
./run.sh uv run ruff check --fix .
```

## Django commands

migrate:
```bash
./run.sh uv run manage.py migrate
```

Create yourself a superuser:
```bash
./run.sh uv run manage.py createsuperuser --username=admin@example.com --email=admin@example.com
```