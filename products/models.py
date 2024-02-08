from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.category

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=254)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_short_description = models.CharField(max_length=254)
    product_long_description = models.TextField(1024)
    product_image_url = models.URLField(1024)
    product_rating = models.URLField(1024)
    category_id = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    
