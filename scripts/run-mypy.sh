#!/usr/bin/env bash

set -o errexit

# Change directory to the project root directory.
cd "$(dirname "$0")"
cd ..

# Install the dependencies into the pre commit mypy environment.
# Note that this can take seconds to run.
pip install --editable . --no-input --quiet

mypy --package iqbacli --config-file pyproject.toml