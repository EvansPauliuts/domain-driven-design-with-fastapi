VENV           = .venv
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))
POETRY         := $(shell command -v poetry 2> /dev/null)

PHONY: lint black lint isort mypy run

black:
	$(POETRY) run black . $(args)

lint:
	poetry run flake8 $(args)

isort:
	poetry run isort . $(args)

mypy:
	poetry run mypy . $(args)

run:
	@echo 'Running app'
	$(POETRY) run uvicorn src.main:app --reload --host 0.0.0.0
