all:

.PHONY: all
all:
	:

.PHONY: check
check:
	nix fmt -- --ci
	poetry check --lock
	poetry install
	cd app/function/m1 && poetry run python -m compileall -q src
	cd app/function/m1 && poetry run python -m unittest discover -s test -t .
	poetry -C app/function-layer/m1 check --lock
	$(MAKE) -C app/function-layer/m1 clean function-layer
	test -d app/function-layer/m1/dist/python

.PHONY: format
format:
	nix fmt
