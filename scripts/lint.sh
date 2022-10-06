#!/usr/bin/env bash

set -e
set -x

isort . --check-only
black . --check
mypy .