#!/usr/bin/env bash
# exit on error
set -o errexit

source .venv/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

export FLASK_APP=run.py
export FLASK_DEBUG=1

flask run
