#!/usr/bin/env -S make -f
pyproject.toml: scripts/generate-pyproject.toml.pl requirements/*.txt
	$^ $@
CITATION.cff: scripts/generate-CITATION.cff.pl pyproject.toml
	$^ $@

.PHONY: build-docs
build-docs:
	cd docs && sphinx-build . _build/html

.PHONY: clean
clean:
	rm -rf docs/_build $(IGNORE_PY) src/*.egg-info dist build
