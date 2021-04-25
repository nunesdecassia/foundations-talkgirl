# GirlTalk - CODE Foundations

Descricao

## Quickstart

Install `pipenv`:

> pip install pipenv

Install all dependencies:

> pipenv install --dev

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
