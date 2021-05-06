# TalkGirl - CODE Foundations Fall 21

An English learning platform for women. The focus of this project was to create the signup and login pages.

## Quickstart

Install `pipenv`:

> pip install pipenv

Install all dependencies:

> pipenv install --dev

Login on GCloud project ([more](https://googleapis.dev/python/google-api-core/latest/auth.html)):

> gcloud auth application-default login

Start the project:

> pipenv run dev

## Scripts

Lint with flask8:

> pipenv run lint

Test with pytest:

> pipenv run test

## Updating 'requirements.txt'

Because Google Cloud needs 'requirements.txt' to install all dependencies,
we must recreate the file every time we add a new production depency, using:

> pipenv lock -r > requirements.txt
