from django.shortcuts import render

# Create your views here.

from coinbase_commerce.client import Client
from django.shortcuts import render

from core import settings


def home_view(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Whiskey',
        'description': 'Sweet sweet nectar.',
        'local_price': {
            'amount': '65.00',
            'currency': 'EUR'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
    }
    charge = client.charge.create(**product)

    return render(request, 'home.html', {
        'charge': charge,
    })