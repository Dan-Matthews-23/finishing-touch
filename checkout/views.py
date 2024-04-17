
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

import stripe
from basket.models import Basket
from checkout.models import OrderLineItem, Orders
from products.models import Products
from accounts.models import UserProfile
from basket.forms import BasketForm

import json






def process_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        order_number=""
        total = 0.00        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],            
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],                        
        }
        profile = get_object_or_404(UserProfile, user=request.user)
        form = BasketForm(request.POST, instance=profile)
        if not form.is_valid():
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
        else:            
            form.save()     
            stripe_id = request.POST.get('client_secret').split('_secret')[0]
            form.stripe_stripe_id = stripe_id
            order = Orders(
                user_profile=profile, 
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone_number = form.cleaned_data['phone_number'],
                postcode = form.cleaned_data['postcode'],
                town_or_city = form.cleaned_data['town_or_city'],
                street_address1 = form.cleaned_data['street_address1'],
                street_address2 = form.cleaned_data['street_address2'],
                county = form.cleaned_data['county'],
                stripe_id =  stripe_id, 
            )
            
            order.save()
            order_total = 0            
            for item in basket:                
                try:
                    product = Products.objects.get(product_id=item['product_id'])                                       
                    if product:
                        line_item_total = float(product.product_price) * int(item['product_quantity'])
                        order_total += line_item_total                        
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item['product_quantity'],
                            order_total=line_item_total 
                        )
                        order_line_item.save()
                        order.order_total = order_total                        
                        order.save()
                    else:
                        return redirect('prepacked_sandwiches')
                        messages.error(request, (
                        "One of the products in your basket wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                        
                except Products.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    form.delete()
            request.session['order_number'] = order.order_number
            total = sum(float(item['price']) for item in basket)
            form_validated = True
            order_created = True
            
            print(f"Order number is {request.session['order_number']}")
            create_payment(request, form_validated, order_created, total)    
        
        if not stripe_public_key:
            messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))
    
    template = 'checkout/checkout.html'
    context = {
        #'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        #'client_secret': intent.client_secret,
        }
    return render(request, template, context)      
    

    

    

def create_payment(request, form_validated, order_created, total):

    
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    basket = request.session.get('basket', {})
    order_number = order_number = request.session['order_number']
    current_bag = basket
    total = sum(float(item['price']) for item in basket)
    #total = 20
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    
    intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            #print(intent)
    template = 'checkout/checkout.html'
    context = {
        #'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)

    
 

 





























def checkout_success(request):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order_number = request.session['order_number']
    form = get_object_or_404(Orders, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the form
        form.user_profile = profile
        form.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': form.phone_number,
                'default_country': form.country,
                'default_postcode': form.postcode,
                'default_town_or_city': form.town_or_city,
                'default_street_address1': form.street_address1,
                'default_street_address2': form.street_address2,
                'default_county': form.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your form number is {order_number}. A confirmation \
        email will be sent to {form.email}.')
    del request.session['order_items']
    del request.session['basket']

    #if 'basket' in request.session:
        #del request.session['basket']

    template = 'checkout/order_confirmed.html'
    context = {
        'form': form,
    }

    return render(request, template, context)





@require_POST
def cache_checkout_data(request):
    try:
        secret_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        stripe.PaymentIntent.modify(
            secret_id, metadata={            
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'There was an error while processing your payment. Please try again in a few minutes.')
        return HttpResponse(content=e, status=400)