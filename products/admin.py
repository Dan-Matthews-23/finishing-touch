from django.contrib import admin
from .models import Products, Category

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_id',       
        'category',
        'display_name',        
    )

    ordering = ('category_id',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'product_id',       
        'product_placeholder_name',
        'product_name',
        'product_price',
        'product_short_description',
        'protein_source',
        'fibre_source',
        'product_image_url',
        'product_rating',
        'category_id',

    )
    ordering = ('product_id',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)


