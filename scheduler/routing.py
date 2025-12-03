from django.urls import path
from .consumer import WorkerConsumer

websocket_urlpatterns = [
    path('ws/worker/<str:worker_id>/', WorkerConsumer.as_view()),
]