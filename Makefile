.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  test to run the tests suit using the local python command"

.PHONY: test
test:
	python3 manage.py test tmw.sites
