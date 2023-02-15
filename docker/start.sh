#!/bin/bash

cd /app

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [PROCESS_TYPE](server)"
    exit 1
fi

PROCESS_TYPE=$1

if [ "$PROCESS_TYPE" = "server" ]; then
    if [ "$DEBUG" = "True" ]; then
        echo ""
        echo "........................................Starting in DEBUG Mode......................................................."
        echo ""
        gunicorn \
            --reload \
            --bind 0.0.0.0:8000 \
            --workers 2 \
            --worker-class eventlet \
            --log-level DEBUG \
            --access-logfile "-" \
            --error-logfile "-" \
            seco.wsgi
    else
        echo ""
        echo "......................................Starting in PRODUCTION Mode..................................................."
        echo ""
        gunicorn \
            --bind 0.0.0.0:8000 \
            --workers 2 \
            --worker-class eventlet \
            --log-level DEBUG \
            --access-logfile "-" \
            --error-logfile "-" \
            seco.wsgi
    fi
fi
