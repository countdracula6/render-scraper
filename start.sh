#!/bin/bash
apt-get update && apt-get install -y chromium-driver chromium
export PATH=$PATH:/usr/lib/chromium/
gunicorn app:app --bind 0.0.0.0:$PORT
