from django.db import models
import uuid

class Basket(models.Model):
    basket_id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    product_id = models.IntegerField(blank=False, editable=False, default=1)
    quantity = models.IntegerField(blank=False, editable=False, default=1)
    default_price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)    

    #def _generate_order_number(self):        
        #return uuid.uuid4().hex.upper()
      

    def __str__(self):
        return self.order_number
    
    

  