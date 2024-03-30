"""

from django.contrib import admin
from .models import Orders#, OrderItems


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
#admin.site.register(OrderPlaceholder, OrderPlaceholderAdmin )
"""






from django.contrib import admin
from .models import Orders, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('order_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total', 'stripe_id')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost', 'order_total', 'stripe_id')

    list_display = ('order_number', 'date', 'full_name','order_total',)

    ordering = ('-date',)


admin.site.register(Orders, OrderAdmin)