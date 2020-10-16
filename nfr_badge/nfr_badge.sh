#!/usr/bin/env sh

DIR=$(cd $(dirname $0); pwd)
export PYTHONPATH="${DIR}/src:${PYTHONPATH}"
>&2 python3 --version
python3 -m nfr_badge "$@"