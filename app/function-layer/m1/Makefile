all:

.PHONY: all
all:
	:


.PHONY: init
init: function-layer


.PHONY: function-layer
function-layer: dist/python


dist/python: requirements.txt
	rm -rf dist
	mkdir -p $@
	poetry run pip install -r requirements.txt --target $@
	rm -rf dist/python/boto*


.PHONY: function-layer.docker
function-layer.docker: requirements.txt
	docker run --platform linux/amd64 --rm -v $(CURDIR):$(CURDIR) -w $(CURDIR) python:3.10 pip install -r requirements.txt --target dist/python
	rm -rf dist/python/boto*


requirements.txt: poetry.lock
	poetry export --without-hashes -f requirements.txt -o $@


.PHONY: clean
clean:
	rm -rf dist requirements.txt .venv
