#!/bin/bash

set -e

repoRoot="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"

echo "Running 'mypy'..."
mypy --config-file "$repoRoot"/.mypy.ini src

echo "Running 'black'..."
black --check \
    --extend-exclude ".python_packages" \
    "$repoRoot"/src

echo "Running 'flake8'..."
flake8 --statistics --config "$repoRoot"/.flake8 "$repoRoot"/src

echo "All checks successfully passed!"
