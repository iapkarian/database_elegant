#!/bin/bash
set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
cd ${DIR}
git pull
find ${DIR} -name '*.pyc' -delete
find ${DIR} -name '__pycache__' -delete
python3 ${DIR}/manage.py collectstatic --noinput
touch ${DIR}/database_elegant/wsgi.py
