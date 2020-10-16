#!/usr/bin/env sh

DIR=$(dirname $(readlink -f "$0"))
export PYTHONPATH="${DIR}/src:${PYTHONPATH}"
python3.8 -m nfr_badge "$@"
