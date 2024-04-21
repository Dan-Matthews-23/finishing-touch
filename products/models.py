from django.db import models
from accounts.models import UserProfile


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

  
        
    def __str__(self):
        return self.display_name

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_placeholder_name = models.CharField(max_length=254,null=True)
    product_name = models.CharField(max_length=254)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_short_description = models.CharField(max_length=254)
    protein_source = models.BooleanField(null=True, blank=True)
    fibre_source = models.BooleanField(null=True, blank=True)    
    product_image_url = models.URLField(1024)    
    category_id = models.IntegerField(default=0)
    calorie_content = models.IntegerField(default=1)
    protein_content = models.DecimalField(max_digits=6, decimal_places=2)
    fibre_content = models.DecimalField(max_digits=6, decimal_places=2)
    fat_content = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_content = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrate_content = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrate_sugar_content = models.DecimalField(max_digits=6, decimal_places=2)
    salt_content = models.DecimalField(max_digits=6, decimal_places=2)
    



    def __str__(self):
        return self.product_name


class Favourites(models.Model):
    favourite_item = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='products')

class ChefMessages(models.Model):
    chef_message = models.TextField(null=False, blank=False, default='')

   
    
    

    
