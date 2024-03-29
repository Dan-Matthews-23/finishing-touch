
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
        order_number = "TESTORDER"

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            #'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'order_number': order_number,
            
        }
        

        profile = get_object_or_404(UserProfile, user=request.user)
        form = BasketForm(request.POST, instance=profile)
        if form.is_valid():            
            form.save()             
            
            pid = request.POST.get('client_secret').split('_secret')[0]
            form.stripe_pid = pid  

            order = Orders(
            user_profile=profile, 
            full_name=form.cleaned_data['full_name'],
            email=form.cleaned_data['email'],
            # ... (assign other fields from cleaned form data) ...
            )
            order.save()  
            
            
            for item in basket:                
                try:
                    product = Products.objects.get(product_id=item['product_id'])
                    print(f"The order_numbers are {item['order_number']}")                    
                    if product:
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item['product_quantity'],
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Products.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    form.delete()
                    return redirect(reverse('view_basket'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            #return redirect('checkout_success',args=[order.order_number])
            template = 'checkout/order_confirmed.html'
            context = {
                                
                    }
            return render(request, template, context)  
            
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request,
                           "There's nothing in your basket at the moment")
            return redirect(reverse('prepacked_sandwiches'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info
        # the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            form = UserProfileForm(instance=profile)

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)



 

































def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    form = get_object_or_404(Order, order_number=order_number)

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

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
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


"""
def create_placeholder(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    order_number = request.session['order_number']
    basket_items = Basket.objects.filter(order_number=order_number)

    total_price = int(float(request.session.get('total_price')))  # Convert to float, then truncate
    
    if basket_items:
        for item in basket_items:
            try:                
                defaults = {
                'quantity': item.quantity,
                'default_price': item.default_price,
                'sub_price': item.sub_price,
                'total_price':total_price,
                'full_name': request.POST['customer_name'],  # Assuming this is correct 
                'email': request.POST['customer_email'],
                'phone_number': request.POST['customer_tel_number'],
                'postcode': request.POST['customer_postcode'],
                'town_or_city': request.POST['customer_address_three'],
                'street_address1': request.POST['customer_address_one'],
                'street_address2': request.POST['customer_address_two'],
                'county': request.POST['customer_address_four'],
                'product_name': item.product_name,
                }
            except Products.DoesNotExist:
                print("Product with id {} not found".format(item.product_id))

            placeholder_item, created = OrderPlaceholder.objects.get_or_create(
                order_number=order_number, 
                product_id=item.product_id,
                defaults=defaults 
            )
            placeholder_item.save()        
    else:
        print("No items found") 

    template = 'checkout/checkout.html'
    context = {       
        'stripe_public_key': stripe_public_key,
        #'defaults_display': defaults_display,
        'defaults': defaults,
        'order_items': basket_items,              
    }

    return render(request, template, context)

"""