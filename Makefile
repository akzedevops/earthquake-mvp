.PHONY: fetch process visualize test

PYTHON ?= python

fetch:
	$(PYTHON) scripts/fetch_data.py --output data/earthquakes_last30.csv

process:
	$(PYTHON) scripts/process_data.py --input data/earthquakes_last30.csv --output data/daily_stats.csv

visualize:
	$(PYTHON) scripts/visualize_map.py --input data/earthquakes_last30.csv --output maps/earthquakes_map.html

test:
	pytest -q
