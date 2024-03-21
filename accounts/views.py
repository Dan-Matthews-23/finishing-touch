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

from checkout.models import Orders


@login_required
def profile(request):
    """ Display the user's profile. """
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


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)