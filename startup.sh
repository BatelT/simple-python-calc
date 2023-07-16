#!/bin/bash
# Install and activate virtual environment
python3 -m pip install --user pip
python3 -m virtualenv calc-venv
source calc-venv/bin/activate
# Install dependencies and build package
pip3 install -r requirements.txt
# Build package
python3 -m build
# Deploy package to local Artifactory repository
python3 setup.py sdist upload -r local