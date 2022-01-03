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
(ecrypto)$ pip install django==3.2.8
(ecrypto)$ django-admin startproject core .
(ecrypto)$ python manage.py startapp payments
```

### Local Environment - Django

- Next step is to registry the application in [settings.py](app/core/settings.py)

```python
# core/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payments.apps.PaymentsConfig'
]
```

- A functional view called home_view was is added to [views.py](app/payments/views.py)

```python
# payments/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html', {})
```

- Create a file inside the payments app named [urls.py](app/payments/urls.py)

```python
# payments/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='payments-home'),
]
```

- The project-level URLs [file](/app/core/urls.py) with the payments app should also be updated

```python
# core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('payments.urls')), # new
    path('admin/', admin.site.urls),
]
```

- A web front should be created. This can be achieved by a HTML homepage in the [templates folder](/app/templates)

```shell
(ecrypto)$ mkdir templates
(ecrypto)$ touch templates/home.html
```

Below is the example HTML that is used to achieve the web front end homepage:

```html
<!-- templates/home.html -->

{% load static %}
<html lang="en">
  <head>
    <title>Django + Coinbase Pay</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>
  </head>
  <body>
    <div class="container mt-5">
      <div class="card w-25">
        <div class="card-body">
          <h3 class="card-title">{{ charge.name }}</h3>
          <img src="static/img/whiskey_1.jpeg" alt="the finest" width="250" height="200">
          <p class="card-text">
            <span>{{ charge.description }}</span>
            <br>
            <span>€{{ charge.pricing.local.amount }} {{ charge.pricing.local.currency }}</span>
          </p>
          <div>
            <a class="btn btn-primary w-100" href="{{ charge.hosted_url }}">Purchase<a>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
```

- At this point Django will not know about this newly created templates folder. As such, this needs to be updated via the [settings.py](/app/core/settings.py)

```python
# core/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        ......
```

### Coinbase Commerce
