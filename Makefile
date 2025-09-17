.PHONY: help test clean

help:
	@echo "Open notebooks in each project to run analyses."

test:
	python -m pytest -q

clean:
	rm -rf **/__pycache__ .pytest_cache
