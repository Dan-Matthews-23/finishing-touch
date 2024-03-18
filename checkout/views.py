from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from checkout.contexts import bag_contents
#from .forms import OrderForm
import stripe
from basket.models import Basket
from .models import OrderPlaceholder, Orders
from products.models import Products





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



def create_placeholder(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    order_number = request.session['order_number']
    basket_items = Basket.objects.filter(order_number=order_number)
    
    if basket_items:
        for item in basket_items:
            try:
                
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
    #print(f"The value of product_name is {product_name}")

    return render(request, template, context)









 


def process_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        #bag = request.session.get('bag', {})
        order_number = request.session['order_number']
        get_order_placeholder = OrderPlaceholder.objects.filter(order_number=order_number)
        get_basket_items = Basket.objects.filter(order_number=order_number)        
        #form_data = request.session['customer_form_details']
       # print(form_data)

        if get_order_placeholder:
            for item in get_order_placeholder:
                defaults = {
                'quantity': item.quantity,
                'default_price': item.default_price,
                'total_price': item.total_price,
                'full_name': item.full_name,  # Assuming this is correct 
                'email': item.email,
                'phone_number': item.phone_number,
                'postcode': item.postcode,
                'town_or_city': item.town_or_city,
                'street_address1': item.street_address1,
                'street_address2': item.street_address2,
                'county': item.county, 
    }
                create_order, created = Orders.objects.get_or_create(
                order_number=order_number, 
                product_id=item.product_id,
                defaults=defaults 
            )
                create_order.save()
                get_order_placeholder.delete()
                get_basket_items.delete()
                
       
    else:
        print("No items found")    
    
    

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
    #print(intent)

    #order_form = OrderForm()
    #print(intent)

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    if 'order_number' in request.session:
        del request.session['order_number']
    if 'total_price' in request.session:
        del request.session['total_price']

    template = 'checkout/order_confirmed.html'
    context = {
        #'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'defaults':defaults,
        
    }

    
    


    return render(request, template, context)