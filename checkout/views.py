from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Orders, OrderLineItem

from products.models import Products
from accounts.models import UserProfile
from accounts.forms import UserProfileForm


import stripe
import json

def render_basket_form(request): 
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY   
    order_form = OrderForm()
    try:
        if request.user.is_authenticated:
            profile = request.user.userprofile  
            form = OrderForm(instance=profile)             
        else:
            form = OrderForm()            
    except Exception as e:  
        logger.error(f"Error processing order: {e}") 
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key':stripe_public_key,
            'client_secret':stripe_secret_key,               
            }                   
    return render(request, template, context)



def process_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        print(request.POST)  # Inspect the raw POST data
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket():
                try:
                    product = Products.objects.get(product_id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
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
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(f" total is {total}")
        print(f" stripe_total is {stripe_total}")
        print(f" stripe.api_key is {stripe.api_key}")
        print(f" intent is {intent}")

        # Attempt to prefill the form with any info the user maintains in their profile
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
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    print(f" order_form is {order_form}")
    print(f" stripe_public_key is {stripe_public_key}")
    print(f" client_secret is {client_secret}")
    print(f" intent is {intent}")

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)










import logging
import json
import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse  # For more structured error responses
from django.contrib import messages

logger = logging.getLogger(__name__)  # Set up a logger for this function

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Log the basket data for debugging
        logger.debug("Basket data: %s", request.session.get('basket', {}))

        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,  # Assuming request.user is a valid string
        })

        return HttpResponse(status=200)

    except stripe.error.StripeError as e:  # Catch specific Stripe errors
        logger.error("Stripe error: %s", e)
        messages.error(request, 'There was a problem with your payment. Please check your card details or try again later.')
        return JsonResponse({'error': str(e)}, status=400)

    except KeyError:  # Catch potential error if 'client_secret' is not found
        logger.error("KeyError: 'client_secret' not found in POST data")
        messages.error(request, 'There was a problem processing your payment. Please refresh the page and try again.')
        return JsonResponse({'error': 'Invalid payment data'}, status=400)

    except Exception as e:  # Catch-all for other unexpected errors
        logger.exception("Unexpected error: %s", e)  # Log the full traceback
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return JsonResponse({'error': 'Internal server error'}, status=500)















def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/order_confirmed.html'
    context = {
        'order': order,
    }

    return render(request, template, context)