# CryptoExchange

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
Feel free to switch this to: [Pipenv](https://pipenv.pypa.io/en/latest/) or perhaps [Poetry](https://python-poetry.org/)

```shell
(ecrypto)$ pip install django==3.2.10
(ecrypto)$ django-admin startproject core .
(ecrypto)$ python manage.py startapp payments
```

### Local Environment - Django, Home Page & Coinbase

Please refer to the project [Wiki page](https://github.com/endk17/cryptoexchange/wiki) for further details
