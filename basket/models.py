from django.db import models

class Basket(models.Model):
    basket_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)    
    product_id = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)  

    def __str__(self):
        return self.basket_id
    
    

    