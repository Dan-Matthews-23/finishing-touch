from django.contrib import admin
from .models import Basket, BasketItem

# Register your models here.
class BasketAdmin(admin.ModelAdmin):
    list_display = (
    'basket_id',
    'order_number',
    'product_id',
    'product_name', 
    'quantity',
    'default_price',
    'sub_price',
    'total_price',    
    )
    ordering = ('basket_id',)

class BasketItemAdmin(admin.ModelAdmin):
    list_display = (
    'basket',
    'product_id',
    'product_name',
    'default_price', 
    'quantity',
    'sub_total',    
    )
    ordering = ('basket',)




admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem, BasketItemAdmin)


