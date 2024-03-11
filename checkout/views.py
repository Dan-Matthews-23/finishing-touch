from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from checkout.contexts import bag_contents
from .forms import OrderForm
import stripe
from basket.models import Basket
from .models import OrderPlaceholder





## STRIPE IS NOW WORKING AGAIN. THERE IS SOMETHING IN THE PART 7 TUTORIAL VIDEO THAT BREAKS THE CODE (  'client_secret': intent.client_secret, ). INTENT NO LONGER WORKS




def create_placeholder(request):
    order_number = request.session['order_number']
    basket_items = Basket.objects.filter(order_number=order_number)

    if basket_items:
        for item in basket_items:
            defaults = {
            'quantity': item.quantity,
            'default_price': item.default_price,
            'total_price': item.total_price,
            'full_name': request.POST['customer_name'],  # Assuming this is correct 
            'email': request.POST['customer_email'],
            'phone_number': request.POST['customer_tel_number'],
            'postcode': request.POST['customer_postcode'],
            'town_or_city': request.POST['customer_address_three'],
            'street_address1': request.POST['customer_address_one'],
            'street_address2': request.POST['customer_address_two'],
            'county': request.POST['customer_address_four'], 
}

         

            placeholder_item, created = OrderPlaceholder.objects.get_or_create(
                order_number=order_number, 
                product_id=item.product_id,
                defaults=defaults 
            )
            placeholder_item.save()

        print("Order placed!") 
        print("Yes, items were found")
    else:
        print("No items found") 

    return render(request, 'checkout/checkout.html') 
















"""

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
    order_number = request.session['order_number']

    basket_items = Basket.objects.filter(order_number=order_number)
    if basket_items.exists():
        for item in basket_items:
            check_existing_order = OrderPlaceholder.objects.filter(order_number=order_number)
            if check_existing_order.exists:
                check_existing_order.order_number = order_number,
                check_existing_order.product_id = item.product_id,
                check_existing_order.quantity =  item.quantity,
                check_existing_order.default_price =  item.default_price,
                check_existing_order.total_price =  item.total_price,
                check_existing_order.full_name = form_data['full_name'],
                check_existing_order.email = form_data['email'],
                check_existing_order.phone_number = form_data['phone_number'],
                check_existing_order.postcode = form_data['postcode'],
                check_existing_order.town_or_city = form_data['town_or_city'],
                check_existing_order.street_address1 = form_data['street_address1'],
                check_existing_order.street_address2 = form_data['street_address2'],
                check_existing_order.county = form_data['county'],
                check_existing_order.save()
            else:
                create_placeholder_item = OrderPlaceholder.objects.create(
                order_number = order_number,
                product_id = item.product_id,
                quantity =  item.quantity,
                default_price =  item.default_price,
                total_price =  item.total_price,
                full_name = form_data['full_name'],
                email = form_data['email'],
                phone_number = form_data['phone_number'],
                postcode = form_data['postcode'],
                town_or_city = form_data['town_or_city'],
                street_address1 = form_data['street_address1'],
                street_address2 = form_data['street_address2'],
                county = form_data['county'],
                ) 
                create_placeholder_item.save()
                print("Order placed!")          
                print("Yes, items were found")
        # Process each basket item
    else:
        print("No items found")   
    return render(request, 'checkout/checkout.html')

"""




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