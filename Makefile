.PHONY: all tests clean

install-dev:
	pip install pre-commit
	pre-commit install
	pre-commit install --hook-type pre-push
	make build-dev

build-dev:
	pip install --no-cache-dir -U pip poetry
	poetry install

tests:
	poetry run python -m pytest -v tests

format:
	poetry run isort src
	poetry run black src

check:
	poetry run isort src -c
	poetry run black src --check
	poetry run pylint src