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

# 1. Compiles client/server-side code
# 2. Fixes the generated protobuf relative import error
proto:
	python3 -m grpc_tools.protoc -I=protos/ --python_out=src/proto --grpc_python_out=src/proto protos/*.proto
	cd src/proto && sed -i '' 's/^\(import.*pb2\)/from . \1/g' *.py

start:
	python3 src/main.py	