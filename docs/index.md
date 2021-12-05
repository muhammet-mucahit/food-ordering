# food-ordering

[![Build Status](https://travis-ci.org/muhammet_mucahit/food-ordering.svg?branch=master)](https://travis-ci.org/muhammet_mucahit/food-ordering)

A small app with capabilities ordering food and listing them.

# Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up --build
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

Initialize database with example data:

```bash
docker-compose run --rm web ./manage.py initialize_data
```

# See Code Style

See code coverage report:

```bash
docker-compose run --rm web coverage run manage.py test
docker-compose run --rm web coverage report
```

See flake8:

```bash
docker-compose run --rm web flake8
```

See black:

```bash
docker-compose run --rm web black --check . # Just control and print will be formatted files
docker-compose run --rm web black .         # Reformat all files with the rules of pyproject.toml
```

The project doesn't use **_pre-commit_**, but if needed it can be used with the config files.