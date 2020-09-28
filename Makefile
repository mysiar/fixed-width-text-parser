SHELL := /bin/bash

test:
	. venv/bin/activate
	python -m unittest discover
.PHONY: test