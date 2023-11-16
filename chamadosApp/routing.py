
from django.urls import path

from . import consumers

websocket_urlspatters = [
    path("", consumers.OSConsumer.as_asgi())
]
