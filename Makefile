SHELL := /bin/bash


ifeq ($(uname_S), Windows)
    venv\Scripts\activate.bat
endif

ifeq ($(uname_S), Linux)
    . venv/bin/activate
endif

test:
	python -m unittest discover tests
.PHONY: test

lint:
	pylint *.py --ignore-patterns=test_.*?py,__init*
.PHONY: lint

dist:
	python3 setup.py sdist bdist_wheel
.PHONY: dist

dist-upload-test:
	python3 -m twine upload --repository testpypi dist/*
.PHONY:dist-upload-test

dist-upload:
	python3 -m twine upload --repository pypi dist/*
.PHONY: dist-upload