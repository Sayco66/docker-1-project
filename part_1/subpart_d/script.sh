#!/bin/bash
set -e
exec python3 process_data.py &
exec python3 app.py