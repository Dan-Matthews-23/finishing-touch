
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
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=2.00)
    order_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)

    def _generate_order_number(self):        
        return uuid.uuid4().hex.upper()

    def update_total(self):        
        self.order_total = self.lineitems.aggregate(Sum('total_cost'))['total_cost__sum']       
        
        #if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
        #    self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
       # else:
        #    self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):      
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderPlaceholder(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    product_id = models.IntegerField(blank=False, editable=False, default=1)
    quantity = models.IntegerField(blank=False, editable=False, default=1)
    default_price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    full_name = models.CharField(max_length=50,blank=False, default="Test")
    email = models.CharField(max_length=50, blank=False, default="Test")
    phone_number = models.CharField(max_length=50, blank=False, default="Test")
    postcode = models.CharField(max_length=50, blank=False, default="Test")
    town_or_city = models.CharField(max_length=50, blank=False, default="Test")
    street_address1 = models.CharField(max_length=50, blank=False, default="Test")
    street_address2 = models.CharField(max_length=50, blank=False, default="Test")
    county = models.CharField(max_length=50, blank=False, default="Test")

    def __str__(self):
        return self.order_number

    #def save(self, *args, **kwargs):       
        #self.total_cost = self.product.price * self.quantity
        #super().save(*args, **kwargs)

    #def __str__(self):
        #return f'SKU {self.product.sku} on order {self.order.order_number}'