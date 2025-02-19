#!/bin/bash
set -e
echo "Starting FastAPI in Docker..."
poetry install --no-interaction --no-ansi --no-root
exec "$@"
