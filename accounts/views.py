from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile







@login_required
def showOrders(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    #user_details = {
        #'user': profile.user.username,  
        #'user' : profile.user,
        #'username': profile.user.username,
        #'default_phone_number': profile.default_phone_number,    
        #'default_postcode': profile.default_postcode,
        #'default_town_or_city': profile.default_town_or_city, 
        #'default_street_address1': profile.default_street_address1,
        #'default_street_address2': profile.default_street_address2,
        #'default_county': profile.default_county,   
        # 
        # #}
    orders = profile.orders.all()

    template = 'account/profile.html'
    context = { 
        #'user_details': user_details,    
        'orders': orders,
        'profile': profile,              
    }
    print(f"The order details is {profile}")
   

    return render(request, template, context)
