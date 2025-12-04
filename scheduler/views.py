from django.http import HttpResponse
from django.shortcuts import render
from .models import Order, ActivityLog

# Create your views here.
def index(request):
    log = ActivityLog.objects.order_by('-timestamp')
    lines = [f"[{entry.timestamp}] {entry.message}" for entry in log]
    return HttpResponse(f"Scheduler Activity: \n" + "\n".join(lines), content_type="text/plain")

def submit_order(request, product_id, qty):
    order = Order.objects.create(id=product_id, quantity=qty, status='pending')
    return HttpResponse(f"Order {order.id} submitted.")