venv:
	python3 -m venv venv
	source ./venv/bin/activate
	python3 -m pip install -r requirements.txt

build:
	docker build -t proxies_scraper:latest .
