SHELL               := /bin/bash

VENV                := .venv
VENV_PYTHON         := $(VENV)/bin/python
SYSTEM_PYTHON       := $(or $(shell which python3), $(shell which python))
PYTHON              := $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))
POETRY              := $(shell command -v poetry 2> /dev/null)
DOCKER_COMPOSE_FILE := docker-compose.yml

.PHONY: lint black lint isort mypy requirements

black:
	$(POETRY) run black . $(args)

lint:
	$(POETRY) run flake8 $(args)

isort:
	$(POETRY) run isort . $(args)

mypy:
	$(POETRY) run mypy . $(args)

requirements:
	$(POETRY) export --without-hashes --only main -f requirements.txt -o requirements.txt

.PHONY: build run stop rm clean

build:
	docker-compose -f $(DOCKER_COMPOSE_FILE) build

run:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d

stop:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

rm:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down -v --remove-orphans

clean:
	docker system prune -af --volumes
	docker network prune -f

.PHONY: run

run:
	@echo 'Running app'
	$(POETRY) run uvicorn src.main:app --reload --host 0.0.0.0

.PHONY: autoupdate

autoupdate:
	pre-commit autoupdate
