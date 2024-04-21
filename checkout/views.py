from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from basket.forms import OrderForm
from .models import Orders, OrderLineItem

from products.models import Products
from accounts.models import UserProfile
from accounts.forms import UserProfileForm


import stripe
import json
import logging
import uuid
logger = logging.getLogger(__name__)  # Uses the current module's name



@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        
        return HttpResponse(status=200)
        
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)



def process_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
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
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
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
        get_order_data = request.session.get('order_items')
        if get_order_data:  
            order_data = [] 
            for product_id, product_details in get_order_data.items():                
                get_product = Products.objects.get(product_id=product_id) 
                order_item = {
                            'product_id': int(product_id),  # Use the iterated product_id
                            'product_quantity': int(product_details['quantity']),
                            'price': float(product_details['cost']),
                            'product_name':  get_product.product_name,            
                        }
                order_data.append(order_item)              
            logger.debug(f"Received order_data: {order_data}")           
            
            if order_data is None or len(order_data) == 0:
                logger.debug(f"Received order_data: {order_data}")
                messages.error(request, "Your basket is empty.")
                logger.info("Empty order data detected")                   
                return redirect('prepacked_sandwiches')              
            else:
                order_number =  uuid.uuid4().hex.upper()
                for order in order_data:
                    order['order_number'] = order_number                                                         
                request.session['basket'] = order_data
                basket_session = request.session['basket']      
        basket = request.session.get('basket', {})    
        profile = get_object_or_404(UserProfile, user=request.user)
        form = OrderForm(request.POST, instance=profile)
        stripe_id = request.POST.get('client_secret').split('_secret')[0]
        form.stripe_stripe_id = stripe_id
        order_number=""
        total = 0.00
        order_total = 0 
        order = Orders(
                    user_profile=profile, 
                    full_name=form_data['full_name'],
                    email=form_data['email'],
                    phone_number = form_data['phone_number'],
                    postcode = form_data['postcode'],
                    town_or_city = form_data['town_or_city'],
                    street_address1 = form_data['street_address1'],
                    street_address2 = form_data['street_address2'],
                    county = form_data['county'],
                    stripe_id =  stripe_id, 
                )            
        order.save()
        request.session['order_number'] = order.order_number
        order_number = request.session['order_number']    
        for item in basket:
            product = Products.objects.get(product_id=item['product_id'])
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
            total = sum(float(item['price']) for item in basket)
            stripe_total = round(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )
        
            template = 'checkout/checkout.html'
            
            context = {
                'form_data': form_data,
            'order_form': order_form,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,   
            }
            
            return render(request, template, context)
    else:
        template = 'checkout/checkout.html'
       
        context = {
            'form_data': form_data,
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.stripe_secret_key,    
            }
        print(f" GET section client secret is {intent.stripe_secret_key}")
        return render(request, template, context)


























def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Orders, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'phone_number': order.phone_number,               
                'postcode': order.postcode,
                'town_or_city': order.town_or_city,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if request.session['basket']:
        del request.session['basket']

    template = 'checkout/order_confirmed.html'
    context = {
        'order': order,
    }

    return render(request, template, context)