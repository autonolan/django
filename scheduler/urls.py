from django.urls import path
from .views import index, submit_order

urlpatterns = [
    path("", index),
    path("submit-order/<str:product_id>/<int:qty>", submit_order),
]
