Restapi-app
======

Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the master branch. ::

    # clone the repository
    git clone https://github.com/ddabberu/python-utils
    # checkout the correct version
    git tag  # shows the tagged versions
    git checkout latest-tag-found-above
    cd restapi-app

Create a virtualenv and activate it::

    python3 -m venv venv
    . venv/bin/activate

Or on Windows cmd::

    py -3 -m venv venv
    venv\Scripts\activate.bat

Install restapi-app::

    pip install -e .

Or if you are using the master branch, install Flask from source before
installing restapi-app::

    pip install -e ../..
    pip install -e .


Run
---

::

    export FLASK_APP=app
    export FLASK_ENV=development
    flask run

Or on Windows cmd::

    set FLASK_APP=app
    set FLASK_ENV=development
    flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    pip install '.[test]'
    pytest


Run with coverage report::

    coverage run -m pytest
    coverage report
    coverage html  # open htmlcov/index.html in a browser

Package for production
----------------------
Running setup.py with Python gives you a command line tool to issue build-related commands. The bdist_wheel command will build a wheel distribution file.

Packaing instructions::

    pip install wheel
    python setup.py bdist_wheel

You can find the file in **dist/app-1.0.0-py3-none-any.whl** The file name is the name of the project, the version, and some tags about the file can install.Copy this file to another machine, set up a new virtualenv, then install the file with pip.


    pip install app-1.0.0-py3-none-any.whl
