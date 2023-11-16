"""
ASGI config for chamadosTI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chamadosTI.settings')

application = get_asgi_application()

import chamadosApp.routing

application = ProtocolTypeRouter({
    'http': application,
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(chamadosApp.routing.websocket_urlspatters)))
})
