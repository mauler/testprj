.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  run 	 					to quickly setup the a local setup and run the server"
	@echo "  test 						to run the tests suit using the local python command"
	@echo "  install_dependencies 		to install dependencies on your current python3 command via pip"

.PHONY: test
install_dependencies:
	python3 -m pip install -r requirements/development.txt

.PHONY: test
test: install_dependencies
	python3 -m pytest

.PHONY: quick-run
run: install_dependencies
	python3 manage.py migrate
	python3 manage.py loaddata initial_data
	python3 manage.py runserver
