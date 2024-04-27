from django.db import models
from products.models import Products
from accounts.models import UserProfile
import uuid
import datetime


class Basket(models.Model):
    basket_id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='basket')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    product_name = models.CharField(max_length=32,
                                    null=False, editable=False, default="Test")
    product_id = models.IntegerField(blank=False, editable=False, default=1)
    quantity = models.IntegerField(blank=False, editable=False, default=1)
    default_price = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        blank=False, default=0)
    sub_price = models.DecimalField(max_digits=6,
                                    decimal_places=2, blank=False, default=0)
    total_price = models.DecimalField(max_digits=6,
                                      decimal_places=2, blank=False, default=0)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE,
                               related_name='items')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='basket_item')
    product_id = models.IntegerField(blank=False)
    product_name = models.CharField(max_length=32, null=False)
    default_price = models.DecimalField(max_digits=6, decimal_places=2,
                                        blank=False)
    quantity = models.IntegerField(blank=False, default=1)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2,
                                    blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
