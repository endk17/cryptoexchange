import logging

from coinbase_commerce.client import Client
from coinbase_commerce.error import (SignatureVerificationError,
                                     WebhookInvalidPayload)
from coinbase_commerce.webhook import Webhook
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from core import settings


# Create your views here.
def home_view(request):

    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = "http://localhost:8000/"

    hostname = request.get_host().split(":", 1)[0]
    if hostname in ("testserver", "localhost", "127.0.0.1"):
        domain_url = "http://localhost:8000/"
    else:
        domain_url = f"https://{hostname}/"

    product = {
        "name": "₿ig (Ξ)'s Whiskey",
        "description": "Sweet sweet nectar",
        "local_price": {"amount": "5.00", "currency": "EUR"},
        "pricing_type": "fixed_price",
        "redirect_url": domain_url + "success/",
        "cancel_url": domain_url + "cancel/",
        "metadata": {
            "customer_id": request.user.id if request.user.is_authenticated else None,
            "customer_username": request.user.username
            if request.user.is_authenticated
            else None,
        },
    }
    charge = client.charge.create(**product)

    return render(request, "home.html", {"charge": charge, })


def success_view(request):
    return render(request, "success.html", {})


def cancel_view(request):
    return render(request, "cancel.html", {})


@csrf_exempt
@require_http_methods(["POST"])
def coinbase_webhook(request):
    logger = logging.getLogger(__name__)

    request_data = request.body.decode("utf-8")
    request_sig = request.headers.get("X-CC-Webhook-Signature", None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)

        # List of all Coinbase webhook events:
        # https://commerce.coinbase.com/docs/api/#webhooks

        if event["type"] == "charge:confirmed":
            logger.info("Payment confirmed.")

            # ChargesAPI - Attach customer_id metadata to product
            customer_id = event["data"]["metadata"]["customer_id"]
            customer_username = event["data"]["metadata"]["customer_username"]

    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        logger.info("Coinbase Webhook\n" f"Error event: {e}")
        return HttpResponse("Error", status=400)

    logger.info(f"Received event: id={event.id}, type={event.type}")
    return HttpResponse("ok", status=200)


def ping(request):

    request_type = request.is_secure()
    hostname = request.get_host().split(":", 1)[0]
    if hostname in ("testserver", "localhost", "127.0.0.1"):
        domain_url = "localhost:8000/"
    else:
        domain_url = f"https://{hostname}/"

    data = {"ping": "pong!", "hostname": domain_url, "request_type": request_type}

    return JsonResponse(data)
