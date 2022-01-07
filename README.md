# CryptoExchange

[![Docker Build + Push](https://github.com/endk17/cryptoexchange/actions/workflows/docker_build_push_deploy.yml/badge.svg)](https://github.com/endk17/cryptoexchange/actions/workflows/docker_build_push_deploy.yml)
[![Heroku Build + Deploy](https://github.com/endk17/cryptoexchange/actions/workflows/heroku_deploy.yml/badge.svg)](https://github.com/endk17/cryptoexchange/actions/workflows/heroku_deploy.yml)
[![CodeQL](https://github.com/endk17/cryptoexchange/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/endk17/cryptoexchange/actions/workflows/codeql-analysis.yml)


Crypto + Whiskey = 🚀🚀🚀

Your one stop whiskey shop for concocting all your favorite boilermakers


## Set up

### Local Environment - Project

Below is an example of the commands used to perform the initial project set up

```shell
mkdir cryptoexchange && cd cryptoexchange
python3.9 -m venv ecrypto
source env/bin/activate
```

In the above example I am using [venv](https://docs.python.org/3/library/venv.html#module-venv)

Alternatives might include: [Pipenv](https://pipenv.pypa.io/en/latest/) or perhaps [Poetry](https://python-poetry.org/)

```shell
(ecrypto)$ pip install django==3.2.10
(ecrypto)$ django-admin startproject core .
(ecrypto)$ python manage.py startapp payments
```

### Local Environment - Django, Home Page & Coinbase

Please refer to the project [Wiki page](https://github.com/endk17/cryptoexchange/wiki) for further details


## Hosting

This is a live POC project this resides on [Heroku](https://www.heroku.com/)

URL: https://fierce-retreat-10367.herokuapp.com


***Note: If any issues or errors are noted please log a GitHub issue for further review and discussion*** 

***WARNING: As this is a publicly hosted application there is an attached cookie web policy which is which correlated to the original creator***
***This should be adjusted to suit your own specific needs if you intend to utilise this solution elsewhere***


## External Comments
