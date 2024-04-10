from .models import UserProfile
from .forms import BasketForm
from .models import Basket
from products.models import Products
from accounts.models import UserProfile
import json
from django import forms
import uuid
import logging
from django.db import transaction
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required





logger = logging.getLogger(__name__)  # Set up basic logging

@require_POST  # Only allow POST requests
@login_required(login_url=settings.LOGIN_URL)
def process_order(request):
    logger.debug("order_data received")
    if request.method == "POST":
        try:
            get_order_data = request.session.get('order_items')  

            if get_order_data:  # Check if order items exist
                order_data = []  # Create a list to hold individual order items

                for product_id, product_details in get_order_data.items():
                    #print(f"The product_id is {product_id}")
                    get_product = Products.objects.get(product_id=product_id)

                    order_item = {
                        'product_id': int(product_id),  # Use the iterated product_id
                        'product_quantity': int(product_details['quantity']),
                        'price': float(product_details['cost']),
                        'product_name':  get_product.product_name,            
                    }
                    order_data.append(order_item)

                #print(order_data)
                logger.debug(f"Received order_data: {order_data}") 
            # Basket handling
           
                if order_data is None or len(order_data) == 0:
                    logger.debug(f"Received order_data: {order_data}")
                    messages.error(request, "Your basket is empty.")
                    logger.info("Empty order data detected")
                    # ... Handle UUID if needed
                    return redirect('prepacked_sandwiches')              
                else:
                    order_number =  uuid.uuid4().hex.upper()
                    for order in order_data:
                        order['order_number'] = order_number  # Same number for all 
                        # To give each order a unique number, generate order_number inside the loop                                         
                    request.session['basket'] = order_data
                    basket_session = request.session['basket']
                    #print(basket_session)
                    # profile = get_object_or_404(UserProfile, user=request.user)                  
                    if request.user.is_authenticated:
                        profile = request.user.userprofile  # Access connected UserProfile
                        form = BasketForm(instance=profile)  # Pre-populate the form
                    else:
                        form = BasketForm()
                                #orders = profile.orders.all()
                    template = 'basket/basket.html'
                    context = {
                        'form': form,
                        'basket': basket_session,        
                    }
                   
                    return render(request, template, context)                        
                                       

                    
                    """
                    Code here
                    """
                    #return render(request, template, context) 
                            

            else:
                # Handle the case where there are no order items
                logger.info("Empty order data detected")
                messages.error(request, "Your basket is empty.")
                return redirect('prepacked_sandwiches')

        except Exception as e:  # Add appropriate exception handling
            logger.error(f"Error processing order: {e}")
            # Handle errors gracefully, e.g., redirect with error message        

    elif request.method == "GET": 
        return render(request, 'basket/basket.html') 

 
"""

basket, created = Basket.objects.get_or_create(
                        user_profile=request.user.userprofile,
                        defaults={'order_number': uuid.uuid4().hex.upper()}
                    )
                    logger.debug(f"Full order_data: {order_data}")
                    print(f"The basket code works fine")

                    # Enhanced data validation (assuming 'quantity' is required)
                    for item_data in order_data:

                        with transaction.atomic(): 
                            product_ids = [item['product_id'] for item in order_data]
                            products = Products.objects.filter(product_id__in=product_ids).prefetch_related('items')

                            if 'product_id' not in item_data or 'quantity' not in item_data:
                                logger.info("There is no product or quantity in item data (line 47 and 48)")
                                raise ValueError("Invalid order item data")                            
                                return redirect('prepacked_sandwiches') 

                            if not isinstance(item_data['quantity'], int) or item_data['quantity'] <= 0:
                                logger.info("There is no product or quantity in item data (line 47 and 48)")
                                raise ValueError("Invalid quantity")                            
                                return redirect('prepacked_sandwiches') 
                    
                        

                            order_items = []  # Collect validated order items
                            total_price = 0

                            for item_data in order_data:
                                logger.debug(f"Processing item: {item_data}") 
                                product = get_object_or_404(Products, product_id=item_data['product_id'])
                                order_item = OrderItem(
                                    basket=basket,
                                    product=product,
                                    product_name=product.name,
                                    price=product.price,
                                    quantity=item_data['quantity']
                                )
                                order_items.append(order_item)
                                total_price += order_item.price * order_item.quantity

                            # Bulk create validated items for efficiency
                            OrderItem.objects.bulk_create(order_items)

                            order_number = basket.order_number  # Retrieve generated order number
                            order = Order( 
                                basket=basket,
                                total_price=total_price,
                                order_number=order_number
                            )
                            order.save()

                            request.session['order_number'] = str(order_number)
                            request.session['order_id'] = order.id

                            basket.delete()  # Clear the basket
                            """




































































# BaCKUP FUNCTION AS OF 23/03
"""
@require_POST  # Only allow POST requests
@login_required(login_url=settings.LOGIN_URL)
def process_order(request):
    if request.method == "POST":
        try:
            # Input Validation
            order_data = json.loads(request.POST.get("orderData"))
            if 'orderData' not in request.POST:
                raise ValueError("Missing orderData")

            # Ensure basket belongs to the user
            basket, created = Basket.objects.get_or_create(
                user_profile=request.user.userprofile,
                defaults={'order_number': uuid.uuid4().hex.upper()}  
            )

            # Enhanced data validation (assuming 'quantity' is required)
            for item_data in order_data:
                if 'product_id' not in item_data or 'quantity' not in item_data:
                    raise ValueError("Invalid order item data")
                if not isinstance(item_data['quantity'], int) or item_data['quantity'] <= 0:
                    raise ValueError("Invalid quantity")

            with transaction.atomic(): 
                product_ids = [item['product_id'] for item in order_data]
                products = Products.objects.filter(product_id__in=product_ids).prefetch_related('items')

                order_items = []  # Collect validated order items
                total_price = 0

                for item_data in order_data:
                    product = get_object_or_404(Products, product_id=item_data['product_id'])
                    order_item = OrderItem(
                        basket=basket,
                        product=product,
                        product_name=product.name,
                        price=product.price,
                        quantity=item_data['quantity']
                    )
                    order_items.append(order_item)
                    total_price += order_item.price * order_item.quantity

                # Bulk create validated items for efficiency
                OrderItem.objects.bulk_create(order_items)

                order_number = basket.order_number  # Retrieve generated order number
                order = Order( 
                    basket=basket,
                    total_price=total_price,
                    order_number=order_number
                )
                order.save()

                request.session['order_number'] = str(order_number)
                request.session['order_id'] = order.id

                basket.delete()  # Clear the basket

            messages.success(request, "Order placed successfully!")
            return JsonResponse({
                'order_number': str(order_number),
                'total_price': total_price,
            })

        except (Products.DoesNotExist, ValueError, json.JSONDecodeError) as e:
            messages.error(request, f"Order processing failed: {str(e)}")
            return render(request, 'basket/basket.html') 
        
        # If order processing was successful, return the JsonResponse
        return JsonResponse({
            'order_number': str(order_number),
            'total_price': total_price,
        })    

    elif request.method == "GET":
        # Assuming you have a way to render the basket from the session
        return render(request, 'basket/basket.html') 
    """

