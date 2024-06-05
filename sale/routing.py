from django.urls import path
from core import consumers

urlrouters = [
    path('sale_channel/', consumers.SaleConsumer.as_asgi())
]
