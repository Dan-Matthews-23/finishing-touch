from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
import logging
import json
import stripe
from django.conf import settings
from django.http import JsonResponse
import stripe
import json
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from django.shortcuts import render, redirect

"""
This function renders the basket
"""


def view_basket(request):
    order_form = OrderForm()
    basket = request.session.get('basket', {})
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
    order_form = order_form
    template = 'basket/basket.html'
    context = {
            'basket': basket,
            'order_form': order_form,
    }
    return render(request, template, context)
