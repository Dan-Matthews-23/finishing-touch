"""


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
"""

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Orders, Reviews


@login_required
def profile(request):  
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'account/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    
    for order in orders:
        order_reviews = order.reviews.all()
        #print(order.order_number) 
        #print(order.reviews.all())
    print(orders)
    

    template = 'account/order_history.html'
    context = {
        'orders': orders,
        #'reviews': reviews,
       
    }

    return render(request, template, context)