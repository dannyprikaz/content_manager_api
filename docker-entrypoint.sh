#!/bin/sh

/usr/local/bin/uwsgi --http 0.0.0.0:8000 --wsgi-file main/__init__.py \
    --callable app --processes 4
