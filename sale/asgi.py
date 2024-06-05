import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from sale.routing import urlrouters

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sale.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(urlrouters)
})
