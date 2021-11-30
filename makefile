client:
	cd web
	yarn dev

export-python-lib:
	pip freeze >> requirements.txt
