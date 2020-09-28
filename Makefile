SHELL := /bin/bash

test:
	. venv/bin/activate
	python -m unittest discover
.PHONY: test

lint:
	pylint *.py --ignore-patterns=test_.*?py,__init*
.PHONY: lint

