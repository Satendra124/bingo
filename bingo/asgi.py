"""
ASGI config for bingo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from bingo_game.consumer import LiveGame
import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bingo.settings')

application = get_asgi_application()

ws_pattern = [
    path('ws/live/<game_id>',LiveGame.as_asgi())
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(ws_pattern),
})
