from .models import Basket
from products.models import Products
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



# Create your views here.

"""
('[{"product_id":"6","product_name":"Egg Mayonnaise","default_price":2.4,"price":"2.40","product_quantity":1,"price_calc":2.4}]') 
"""

def basket(request, context):
    return render(request, 'basket/basket.html')




















logger = logging.getLogger(__name__)  # Set up basic logging

@require_POST  # Only allow POST requests
@login_required(login_url=settings.LOGIN_URL)
def process_order(request):
    if request.method == "POST":
        try:
            order_data = json.loads(request.POST.get("orderData"))
            logger.debug(f"Received order_data: {order_data}")  # Log the data
            # Basket handling
            try:
                basket, created = Basket.objects.get_or_create(
                    user_profile=request.user.userprofile,
                    defaults={'order_number': uuid.uuid4().hex.upper()}
                )
            except Exception as e:  
                messages.error(request, f"There was an error associating your basket: {e}")
                return render(request, 'basket/basket.html')

            if order_data is None or len(order_data) == 0:
                messages.error(request, "Your basket is empty.")
                logger.info("Empty order data detected")

                # ... Handle UUID if needed

                return redirect('prepacked_sandwiches')  

        except json.JSONDecodeError:
            messages.error(request, "Invalid order data format. Please check and try again.")
            logger.warning("JSON decoding error") 
            return render(request, 'basket/basket.html') 

        except ValueError:  
            messages.error(request, "Your order data is missing. Please try again.")
            logger.warning("Missing 'orderData'")
            return render(request, 'basket/basket.html') 

        logger.warning("Unexpected condition - order data not processed")
        messages.error(request, "An unexpected error occurred. Please try again.") 

    elif request.method == "GET": 
        return render(request, 'basket/basket.html') 

 


   

























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

