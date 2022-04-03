SHELL=/bin/bash

# Installs the environment after checkout
install:
	conda env create -f environment.yaml --prefix ./env

# Updates the environment after updating environment.yml
update:
	conda env update --prefix ./env --file environment.yaml  --prune

activate:
	conda init bash
	conda activate ./env

deactivate:
	conda deactivate

test:
	pytest -q tests/test.py

start:
	python3 -m src.main