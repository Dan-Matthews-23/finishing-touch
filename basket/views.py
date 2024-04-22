from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
import logging
import json
import stripe
from django.conf import settings
from django.http import JsonResponse  # For more structured error responses
import stripe
import json

from accounts.models import UserProfile
from accounts.forms import UserProfileForm

from accounts.models import UserProfile


from django.shortcuts import render, redirect



def view_basket(request):
    order_form = OrderForm()
    basket = request.session.get('basket', {})   
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.full_name,
                'email': profile.user.email,
                'phone_number': profile.phone_number,                
                'postcode': profile.postcode,
                'town_or_city': profile.town_or_city,
                'street_address1': profile.street_address1,
                'street_address2': profile.street_address2,
                'county': profile.county,
                })            
        except UserProfile.DoesNotExist:
                order_form = OrderForm()
    else:
            order_form = OrderForm()     
    template = 'basket/basket.html'
    context = {
        'basket': basket,
        'order_form': order_form,        
    }
    return render(request, template, context)  # Return the rendered response


"""
@require_POST
def update_details(request):
    if request.method == 'POST':        
        profile = get_object_or_404(UserProfile, user=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('process_checkout')  
            else:
                messages.error(request,
                            ('Update failed. Please ensure '
                                    'the form is valid.'))
        else:
                form = UserProfileForm(instance=profile)
        

"""
    