#!/bin/bash
set -e

python -m build
python -m twine upload dist/*
# python -m pip install unicode-segment
