from django.urls import path
from .consumers import WorkerConsumer

websocket_urlpatterns = [
    path('ws/worker/<str:id>/', WorkerConsumer.as_asgi()),
]