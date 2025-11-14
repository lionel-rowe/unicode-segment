#!/bin/bash

set -e

python -m build
python -m twine upload --repository testpypi dist/*
# python -m pip install --index-url https://test.pypi.org/simple/ --no-deps unicode-segment
