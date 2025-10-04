# convenience only
PY = python
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python

OKUN_DATA ?= okun-law/data/raw/labor_panel_sample.csv
FC_DATA ?= unemployment-forecast/data/raw/labor_panel_sample.csv

install:
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

okun:
	@if [ ! -f "$(OKUN_DATA)" ]; then echo "Missing $(OKUN_DATA)"; exit 1; fi
	$(PYTHON) okun-law/src/fit_okun.py --data $(OKUN_DATA)

forecast:
	@if [ ! -f "$(FC_DATA)" ]; then echo "Missing $(FC_DATA)"; exit 1; fi
	$(PYTHON) unemployment-forecast/src/forecast_unemployment.py --data $(FC_DATA)

clean:
	rm -f okun-law/reports/* unemployment-forecast/reports/*
