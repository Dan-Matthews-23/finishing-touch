




from django.contrib import admin
from .models import Orders, OrderLineItem, Reviews


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('order_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total', 'stripe_id')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total', 'stripe_id')

    list_display = ('order_number', 'date', 'full_name','order_total',)

    ordering = ('-date',)


class ReviewsAdmin(admin.ModelAdmin):
    model = Reviews
    list_display = (
        'order',
        'product',
        'stars',
        'review_title',
        'review_body',
    )
    
    
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Orders, OrderAdmin)