#!/usr/bin/env sh

mkdir -p /home/mk/postgres_data
docker compose up -d --build
