#!/usr/bin/env sh

DIR=$(cd $(dirname $0); pwd)
export PYTHONPATH="${DIR}/src:${PYTHONPATH}"
python3.8 -m nfr_badge "$@"