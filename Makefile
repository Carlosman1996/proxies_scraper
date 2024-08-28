venv:
	python3 -m venv venv
	# Clean venv if it exists
	python3 -m venv --clear venv
	source ./venv/bin/activate
	python3 -m pip install -r requirements.txt

build:
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

tox:
	tox

ruff:
	# Automatically fixes code
	ruff check --fix

pre-commit:
	# Install to automatically check code at git commits
	pre-commit install
