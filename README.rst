===================
Running the Project
===================

The only necessary python library at the moment is **django 2.x (python3)** after activating your **virtualenv**, use the command  below:


Quick run
=========

The command below will install the dependencies, create the database, load sample data and run the testing webserver.

    $ make run


Running Tests
=============

The **make test** command will install all dependencies, including testing dependencies.

The tests are executed/discovered by **pytest** and at the end a coverage report is displayed together with pyflakes output.

    $ make test
