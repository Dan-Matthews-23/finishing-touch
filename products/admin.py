from django.contrib import admin
from .models import Products, Category, Favourites

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

class FavouritesAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Get all field names using the model's _meta API
        field_names = [field.name for field in Favourites._meta.fields]
        return field_names
    
    

admin.site.register(Favourites, FavouritesAdmin)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)


