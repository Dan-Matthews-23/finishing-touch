from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Products, Category, Favourites, ChefMessages
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
import json





# Create your views here.
@login_required
# Display all breads
def prepacked_sandwiches(request):   
    sandwich_items = Products.objects.all()
    get_chef_message = ChefMessages.objects.first()
    chef_messages = get_chef_message.chef_message
    
    

    profile = get_object_or_404(UserProfile, user=request.user)
    order_items = request.session.get('order_items')

    # Enhanced favorites logic
    for item in sandwich_items:
        item.is_favourite = Favourites.objects.filter(
            user_profile=profile,
            favourite_item_id=item.product_id
        ).exists()

    context = {
        'sandwich_items': sandwich_items,
        'order_items': 'order_items',
        'chef_messages': chef_messages,
    }
    return render(request, 'products/sandwiches.html', context)

@login_required
def add_to_favourites(request):
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)
        product_id = request.POST['product_id-favourites']
        products = Products.objects.get(product_id=product_id)
        try:
            add_favourite = Favourites(favourite_item=products,user_profile=profile, )
            add_favourite.save()
            print(f"The product ID is {product_id}")
        except Products.DoesNotExist:
            print(f"The product_id does not exist")
        return redirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_from_favourites(request):
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)
        product_id = request.POST['product_id-favourites']

        try:
            # Find the Favourites object to delete
            favourite_to_delete = Favourites.objects.get(
                favourite_item__product_id=product_id,
                user_profile=profile
            )
            favourite_to_delete.delete()  # Delete the object
            print(f"Product ID {product_id} removed from favourites")

        except Favourites.DoesNotExist:
            print(f"Product ID {product_id} not found in favourites")

        return redirect(request.META.get('HTTP_REFERER'))

from decimal import Decimal

@login_required
def add_to_order(request):
  if request.method == 'POST':
    del request.session['order_total']  # Clear previous total
    product_id = request.POST['product_test']
    get_product = Products.objects.get(product_id=product_id)
    quantity = int(request.POST['quantity'])
    product_default_price = get_product.product_price
    cost = Decimal(product_default_price) * quantity  # Use Decimal for accuracy

    # Initialize total cost outside if statements
    total_cost = 0

    # Check if an order already exists in the session
    if 'order_items' in request.session:
      order_items = request.session['order_items']

      # Check if the product is already in the order
      if product_id in order_items:
        # Update existing product quantity
        order_items[product_id]['quantity'] = quantity

        # Calculate total cost for this product
        total_cost = Decimal(product_default_price) * quantity
        order_items[product_id]['cost'] = str(total_cost)

      else:
        # Add as a new order item with total cost
        order_items[product_id] = {
          'product_name': get_product.product_name,
          'quantity': quantity,
          'cost': str(Decimal(product_default_price) * quantity),
        }

    else:
      # Create a new order if it doesn't exist
      order_items = {
        product_id: {
          'product_name': get_product.product_name,
          'quantity': quantity,
          'cost': str(Decimal(product_default_price) * quantity),
        }
      }

    # Update the session and calculate total cost for all items
    request.session['order_items'] = order_items

    # Loop through order items to calculate total cost
    for item_id, item_data in order_items.items():
      item_cost = Decimal(item_data['cost'])  # Convert cost string to Decimal
      total_cost += item_cost

    # Now you have the total cost for all items
    request.session['order_total'] = str(total_cost)
    return redirect(request.META.get('HTTP_REFERER'))



@login_required
def remove_item(request):
    if request.method == 'POST':
        product_id = request.POST['remove-item-product-id']

        # Check if an order already exists in the session
        if 'order_items' in request.session:
            order_items = request.session['order_items']

            # Check if the product is already in the order
            if product_id in order_items:
                # Remove the item from the order_items dictionary
                del order_items[product_id]

                # Recalculate total cost
                total_cost = 0
                for item_id, item_data in order_items.items():
                    item_cost = Decimal(item_data['cost'])
                    total_cost += item_cost

                # Update the session with the modified order_items and total cost
                request.session['order_items'] = order_items
                request.session['order_total'] = str(total_cost)

        print(f"The product_id selected is {product_id}")
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))  # Handle GET requests by returning to the previous page

   
    
    





















def clear_order(request):
    if request.method == 'POST':
        del request.session['order_items']
        return redirect(request.META.get('HTTP_REFERER'))
    





    
        





















"""

def add_to_basket(request):
    # Get form data
    if request.method == 'POST':
        product_id = request.POST.get("increase-quantity") 
        print(f" The value of the button is {product_id}")
    return render(request, 'products/sandwiches.html')
"""



