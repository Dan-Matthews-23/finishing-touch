from django.db import models
from django.db.models import Sum
from django.conf import settings
import uuid
from products.models import Products

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.IntegerField(null=False, blank=False, editable=False)
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    customer_email = models.CharField(max_length=50, null=False, blank=False)
    customer_tel_number = models.CharField(max_length=50, null=False, blank=False)
    customer_address_one = models.CharField(max_length=50, null=False, blank=False)
    customer_address_two = models.CharField(max_length=50, null=False, blank=False)
    customer_address_three = models.CharField(max_length=50, null=False, blank=False)
    customer_address_four = models.CharField(max_length=50)
    customer_postcode = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    order_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)

class OrderPlaceholder:
    order = models.ForeignKey(Orders, null=False, blank=False, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0, editable=False)


