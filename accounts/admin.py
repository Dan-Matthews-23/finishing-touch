from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = (
    'user_id',
    'username',
    'email',
    'contact_number',
    'street_address1',  
    'street_address2',
    'town_or_city',
    'county',
    'postcode',    
    )
    ordering = ('user_id',)  

admin.site.register(Users, UsersAdmin)

