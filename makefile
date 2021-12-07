#!/bin/bash
.PHONY: client export-python-lib

client:
	yarn --cwd web dev

export-python-lib:
	rm requirements.txt
	pip freeze >> requirements.txt

restart-postgres:
	pg_ctl -D "C:\Program Files\PostgreSQL\14\data" restart
