from django.db import models

# Create your models here.


rating_select = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (4, '5'),
    )
 


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
    product_rating = models.IntegerField(choices=rating_select, default=1)
    category_id = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
    
    

    
