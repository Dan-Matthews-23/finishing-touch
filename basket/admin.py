from django.contrib import admin
from .models import Basket

# Register your models here.
class BasketAdmin(admin.ModelAdmin):
    list_display = (
    'basket_id',
    'order_number',
    'product_id', 
    'quantity',
    'default_price',
    'total_price',    
    )
    ordering = ('basket_id',)

admin.site.register(Basket, BasketAdmin)


