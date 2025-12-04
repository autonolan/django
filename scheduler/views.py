from django.http import HttpResponse
from django.shortcuts import render
from .models import Order, ActivityLog

# Create your views here.
def index(request):
    log = ActivityLog.objects.all().order_by('-timestamp')[:10]
    return HttpResponse(f"Scheduler Logger: \n {log}")

def submit_order(request, product_id, qty):
    order = Order.objects.create(id=product_id, quantity=qty, status='pending')
    return HttpResponse(f"Order {order.id} submitted.")