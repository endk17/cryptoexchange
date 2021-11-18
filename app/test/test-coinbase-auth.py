from core import settings
from coinbase_commerce.client import Client
from config import COINBASE_COMMERCE_API_KEY


client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
for charge in client.charge.list_paging_iter():
    print("{!r}".format(charge))