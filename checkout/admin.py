

from django.contrib import admin
from .models import Orders


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',       
        'order_number',
        'customer_name',
        'customer_email',
        'customer_tel_number',
        'customer_address_one',
        'customer_address_two',
        'customer_address_three',
        'customer_address_four',
        'customer_postcode',
        'order_date',
        'delivery_cost',
        'order_cost',
        'total_cost',
    )
    ordering = ('order_id',)  

# Register your models here.
admin.site.register(Orders, OrdersAdmin)
