

from django.contrib import admin
from .models import Orders, OrderPlaceholder


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
    'order_id',
    'order_number',
    'user_profile',
    'product_id',
    'product_name',  
    'quantity',
    'default_price',
    'sub_price',
    'total_price',
    'full_name',
    'email',
    'phone_number',
    'postcode',
    'town_or_city',
    'street_address1', 
    'street_address2',
    'county',
    )




    ordering = ('order_id',)  

# Register your models here.


class OrderPlaceholderAdmin(admin.ModelAdmin):
    list_display = (
    'order_id',
    'order_number',
    'product_id',
    'product_name',  
    'quantity',
    'default_price',
    'sub_price',
    'total_price',
    'full_name',
    'email',
    'phone_number',
    'postcode',
    'town_or_city',
    'street_address1', 
    'street_address2',
    'county',
    )
    ordering = ('order_id',)



admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderPlaceholder, OrderPlaceholderAdmin )