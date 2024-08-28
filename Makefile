venv:
	python3 -m venv venv
	# Clean venv if it exists
	python3 -m venv --clear venv
	source ./venv/bin/activate
	python3 -m pip install -r requirements.txt

poetry:
	# Create venv
	poetry env use python3	# 3.12
	# List venvs
	poetry env list
	# Remove venvs
	poetry env remove --all

	# Initialize poetry in repository
	poetry init
	# Check venv info
	poetry env info
	# Install dependencies from project.toml
	poetry install
	# Activate venv
	poetry shell
	# Install dependencies
	poetry install
	# Add dependencies
	poetry add requests beautifulsoup4	# Install packages with versions specified as '^'
	# Add group dependencies
	poetry add --group dev black flake8 isort mypy pylint	# It can be set as '--optional'.
	# Update/upgrade dependencies
	poetry show --latest --top-level
	# Remove dependencies
	poetry remove requests

	# Run poetry (no activated in shell):
	poetry run python proxies_scraper/main.py
	poetry run ruff

	# Run poetry (activated in shell):
	python proxies_scraper/main.py
	ruff

api-build:
	docker build -t proxies_scraper:latest .

package:
    # Update complete list of dependencies (save in requirements.txt):
	pip-compile pyproject.toml
	pip-compile --extra dev pyproject.toml
    # Install dependencies into venv:
	pip-sync
	# Install optional dependencies:
	python3 -m pip install proxies_scraper[dev]
	# Install package in editable mode:
	python3 -m pip install -e .
	# Create source archive and a wheel for the package
	python3 -m build
	# Check package description
	twine check dist/*
	# Upload package
	twine upload -r testpypi dist/*

package-poetry:
	poetry build
	poetry config pypi-token.pypi <your-token>
	poetry publish

tox:
	tox

ruff:
	# Automatically fixes code
	ruff check --fix

pre-commit:
	# Install to automatically check code at git commits
	pre-commit install
