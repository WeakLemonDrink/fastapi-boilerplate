# Upskilling FastAPI

Following the [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) and committing the result!

## Installation

Follow these steps to install Python and project dependencies. These installation steps could be scripted, but I've deliberately broken them out into steps here so we can understand how and why we're doing this for our dev environment.

1. Open a terminal at the `upskilling-fastapi` project root
2. Install [pyenv](https://github.com/pyenv/pyenv). Pyenv is a Python version manager (like [nvm](https://github.com/nvm-sh/nvm) for [node.js](https://nodejs.org/en/)) that will allow you to install and run different Python versions on your computer. This is useful when we're contributing to different Python projects, which might run different Python versions. We can install pyenv using [brew](https://brew.sh/)
   ```
   $ brew install pyenv
   ```
3. Install [pipenv](https://pipenv.pypa.io/en/latest/). Pipenv is a Python package manager (like [npm](https://www.npmjs.com/) for [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) development). It automatically creates and manages a virtual environment for Python projects, and manages dependencies. We can again install pipenv using brew
   ```
   $ brew install pipenv
   ```
4. Next we install [Python](https://www.python.org/). You probably already have a version of Python on your computer, but the `.python-version` file in the project root defines which Python version we're using for this project. Pyenv will read the file and install the correct Python version for us
   ```
   $ pyenv install
   ```
5. Pyenv should have installed the correct Python version and "selected" this version to be used as part of the `upskilling-fastapi` project. You can check the correct Python version is selected by running
   ```
   $ pyenv version
   ```
6. Now we can create a virtual environment for the `upskilling-fastapi` project and install any project dependencies using pipenv. This action will read the attributes in the `Pipfile` and `Pipfile.lock` and install the right packages and versions we need, which insures we can set the correct dependencies for other devs and when deploying to production. Run
   ```
   $ pipenv install --dev
   ```
7. Activate your newly created virtual environment by running
   ```
   $ pipenv shell
   ```

Now you're ready to follow the tutorial.

## Start the dev server

The FastAPI tutorial uses [uvicorn](https://www.uvicorn.org/) as a development server and to handle asyncronous operations. To start the dev server, run

```
$ uvicorn main:app --app-dir ./app --reload
```

This will make the project available at `http://127.0.0.1:8000` and hot reload when you make any changes.

## Run the tests

The tests for this project are contained within the `tests` folder. Once you have installed the project, you can run the tests by following the steps below:

1. Open a terminal at the `upskilling-fastapi` project root
2. Activate your virtual environment by running
   ```
   $ pipenv shell
   ```
3. Run the tests by running
   ```
   $ pytest
   ```

Pytest will collect and run any tests it finds in the project according to its [test discovery implementation](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html#conventions-for-python-test-discovery).
