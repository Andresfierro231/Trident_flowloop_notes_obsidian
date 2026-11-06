PYTHON ?= python3.11

.PHONY: help check test docs-check references-check package-check

help:
	@echo "TRIDENT repository checks"
	@echo "  make check          Run the required non-mutating local checks"
	@echo "  make test           Run all Python tests"
	@echo "  make docs-check     Audit documentation and coordination state"
	@echo "  make references-check  Verify immutable reference checksums"
	@echo "  make package-check  Build a wheel in a temporary directory"

check:
	$(MAKE) --keep-going test docs-check references-check

test:
	PYTHONPATH=src $(PYTHON) -B -m pytest

docs-check:
	$(PYTHON) -B tools/docs_audit.py --root . --check --strict

references-check:
	$(PYTHON) -B tools/check_references.py --root reference

package-check:
	@package_tmp="$$(mktemp -d)"; \
	trap 'rm -rf "$$package_tmp"' EXIT; \
	mkdir -p "$$package_tmp/source/src" "$$package_tmp/wheel" "$$package_tmp/install"; \
	cp pyproject.toml README.md "$$package_tmp/source/"; \
	cp -R src/trident_thermal "$$package_tmp/source/src/"; \
	cd "$$package_tmp/source" && \
	$(PYTHON) -m pip wheel . --no-deps --no-build-isolation \
		--wheel-dir "$$package_tmp/wheel" && \
	set -- "$$package_tmp"/wheel/*.whl && \
	test "$$#" -eq 1 && \
	$(PYTHON) -m pip install --disable-pip-version-check --no-deps \
		--target "$$package_tmp/install" "$$1" && \
	PYTHONPATH="$$package_tmp/install" $(PYTHON) -c \
		'import trident_thermal; assert trident_thermal.__version__ == "0.0.0"'
