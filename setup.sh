#!/bin/bash -eu
if [ ! -e .venv ]; then
  echo 'creating virtual environment'
  python3 -m venv .venv --prompt=onkyo-music-machine
fi

source .venv/bin/activate
pip install -e .

echo 'omm is installed, switch to the virtual environment with:'
echo 'source .venv/bin/activate'