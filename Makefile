PYTHON ?= python3

.PHONY: init init-ts init-go init-rust check fmt progress doctor show-profile new-module new-feature new-bugfix new-refactor new-decision

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

new-feature:
	@if [ -z "$(name)" ]; then echo "Usage: make new-feature name=<feature-name>"; exit 1; fi
	$(PYTHON) tools/vcflow.py new-change --type feature --name $(name)

new-bugfix:
	@if [ -z "$(name)" ]; then echo "Usage: make new-bugfix name=<bug-name>"; exit 1; fi
	$(PYTHON) tools/vcflow.py new-change --type bugfix --name $(name)

new-refactor:
	@if [ -z "$(name)" ]; then echo "Usage: make new-refactor name=<refactor-name>"; exit 1; fi
	$(PYTHON) tools/vcflow.py new-change --type refactor --name $(name)

new-decision:
	@if [ -z "$(title)" ]; then echo "Usage: make new-decision title=<decision-title>"; exit 1; fi
	$(PYTHON) tools/vcflow.py new-decision --title "$(title)"
