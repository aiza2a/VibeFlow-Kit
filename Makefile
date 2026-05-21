PYTHON ?= python3

.PHONY: init init-ts init-go init-rust check fmt progress doctor show-profile new-module

init:
	$(PYTHON) tools/vcflow.py init --profile python

init-ts:
	$(PYTHON) tools/vcflow.py init --profile typescript

init-go:
	$(PYTHON) tools/vcflow.py init --profile go

init-rust:
	$(PYTHON) tools/vcflow.py init --profile rust

check:
	$(PYTHON) tools/check.py

fmt:
	$(PYTHON) tools/check.py --include-format

progress:
	$(PYTHON) tools/progress.py

doctor:
	$(PYTHON) tools/vcflow.py doctor

show-profile:
	$(PYTHON) tools/vcflow.py show-profile

new-module:
	@if [ -z "$(name)" ]; then echo "Usage: make new-module name=<module-name>"; exit 1; fi
	$(PYTHON) tools/vcflow.py new-module --name $(name)
