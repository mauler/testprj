.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  run 	 	to quickly setup the a local setup and run the server"
	@echo "  test 		to run the tests suit using the local python command"

.PHONY: test
test:
	python3 manage.py test -v 2 tmw.sites

.PHONY: quick-run
run:
	python3 -m pip install -r requirements.txt
	python3 manage.py migrate
	python3 manage.py loaddata initial_data
	python3 manage.py runserver
