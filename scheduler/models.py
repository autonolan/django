from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class Workstation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    current_order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)

class ActivityLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()