from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from checkout.contexts import bag_contents
from .forms import OrderForm
import stripe





## STRIPE IS NOW WORKING AGAIN. THERE IS SOMETHING IN THE PART 7 TUTORIAL VIDEO THAT BREAKS THE CODE (  'client_secret': intent.client_secret, ). INTENT NO LONGER WORKS





















def create_placeholder(request):
    form_data = {
            'full_name': request.POST['customer_name'],
            'email': request.POST['customer_email'],
            'phone_number': request.POST['customer_tel_number'],            
            'postcode': request.POST['customer_postcode'],
            'town_or_city': request.POST['customer_address_three'],
            'street_address1': request.POST['customer_address_one'],
            'street_address2': request.POST['customer_address_two'],
            'county': request.POST['customer_address_four'],
            
        }
    print(form_data)
    request.session['customer_form_details'] = form_data
    return render(request, 'checkout/checkout.html')

def process_checkout(request):

    if request.method == 'POST':
        #bag = request.session.get('bag', {})
        form_data = request.session['customer_form_details']
        print(form_data)

        """
        form_data = {
            'full_name': request.POST['customer_name'],
            'email': request.POST['customer_email'],
            'phone_number': request.POST['customer_tel_number'],            
            'postcode': request.POST['customer_postcode'],
            'town_or_city': request.POST['customer_address_three'],
            'street_address1': request.POST['customer_address_one'],
            'street_address2': request.POST['customer_address_two'],
            'county': request.POST['customer_address_four'],
        }
        """
        #print(form_data)
        
    
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

   # bag = request.session.get('bag', {})
    #if not bag:
        #messages.error(request, "There's nothing in your bag at the moment")
        #return redirect(reverse('prepacked_sandwiches'))

    current_bag = bag_contents(request)
    #total = 10
    total = int(float(request.session.get('total_price')))  # Convert to float, then truncate
    print(total)

    #print(f"The type of total is {type(total)} and its value is {total}")
    
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    order_form = OrderForm()
    #print(intent)

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)