from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('<int:user_id>/', ChatConsumer.as_asgi()),
]
