.PHONY: venv pip run tests

venv:
	python -m venv venv
	source venv/bin/activate

pip:
	pip3 install -r requirements.txt

run:
	python3 main.py

tests:
	python3 -m unittest discover tests
