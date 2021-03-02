# Numerated Coding Challenge

- Joshua Smith
- [Email](joshuawordsmith@gmail.com)
- [Portfolio](https://joshuawordsmith.github.io/portfolio/)

## Introduction

This application will find the next departing train for a particular stop on the MBTA T network.

This project was built using [PyPoetry](https://python-poetry.org/), but it is not required to run it

## Getting started

In order to make requests to the mbta back end you will need an api key from the [MBTA public API](https://api-v3.mbta.com)

Once the API key is obtained, set is as an environment variable called `MBTA_API_KEY`

If you are testing with `unittest`, you may also need to set your `PYTHONPATH` environment variable

for example you could `source` an `.env` file with the following contents:

```sh

export MBTA_API_KEY=<YOUR KEY GOES HERE>
export PYTHONPATH=.:src

```

This project uses `black` as an autoformatter, which follows python `PEP8` standards, but is also pretty opinionated on top of that.

Refer to the `src.services.request_mbta.py` file where `MBTA_API_KEY` is referenced if needed if you have issues getting it to pick up the API key as an environment variable

## Running the application

### Run with Minimum Dependencies

If you are not using [Poetry](https://python-poetry.org/docs/) then you will need to make sure your python interpreter is `3.7` or above and then run `pip install requests`

To start the application you will then run `python main.py`

### Run with poetry

- make sure your python environment (like `pyenv`) is set to 3.7 or above
- refer to the [Poetry installation docs](https://python-poetry.org/docs/) if you don't already have poetry installed installed
- `cd` into the root directory
- run `poetry install`
- run `poetry shell`
- run `python main.py`

## Running Tests

### Running Tests with Minimal Dependencies

The tests only use the python standard library (although they import files which import `requests`) and so they can be run with `unittest`

To run a test file make sure your `PYTHONPATH` includes the `src` directory and run `python -m unittest tests/path/to/file.py`

### Running Tests with Poetry and pytest

- if you haven't already, run `poetry install`
- if you havent activated the virtual environment run `poetry shell`
- to run all the unit tests and see the test coverage by file, run `pytest --cov=src/ tests/`

## Initial Challenge Instructions

### Challenge

> Find the next departing train for a particular stop on the MBTA T network.

### Story Form

As an MBTA rider, I would like to know when the next train is going to depart from a specific stop so that I know when I should plan to get to the boarding area.

### Instructions

Write a program in a language of your choice (we prefer Python or Angular) that interacts with the [MBTA public API](https://api-v3.mbta.com) to achieve the following acceptance criteria:

1. Your program should prompt users to select from a list of routes that service only Light and Heavy Rail trains.
2. Your program should display a listing of stops related to the selected route and prompt the user to select a stop
3. Your program should display a list of route directions and prompt the user to select a direction
4. Your program should display the next predicted departure time for a train based on the previously selected inputs

### Evaluation

Your code submission will be evaluated on:

- function
- code structure
- performance
- readability
- testability
- supplied automated tests

If there are any package dependencies or special install instructions, please make sure to include those with your submission.
