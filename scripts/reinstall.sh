#!/bin/bash
set -eu

### Re-install the package locally

pip uninstall molsimple -y || true
pip install .
rm -rf build molsimple.egg-info
