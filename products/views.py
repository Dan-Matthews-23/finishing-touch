from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Products, Category, Favourites, ChefMessages
from .forms import ProductManagementForm
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages





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
    product_id = request.POST['product_test']
    get_product = Products.objects.get(product_id=product_id)
    quantity = int(request.POST['quantity'])
    product_default_price = get_product.product_price
    cost = Decimal(product_default_price) * quantity  # Use Decimal for accuracy

    # Check if an order already exists in the session
    if 'order_items' in request.session:
      order_items = request.session['order_items']

      # Check if the product is already in the order
      if product_id in order_items:
        # Update existing product quantity
        order_items[product_id]['quantity'] = quantity

        # Calculate total cost for this product (update cost if needed)
        order_items[product_id]['cost'] = str(Decimal(product_default_price) * quantity)
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

    # Update the session (order items already updated)
    request.session['order_items'] = order_items

    # Calculate total cost for all items (moved outside loops)
    total_cost = 0
    for item_id, item_data in order_items.items():
      item_cost = Decimal(item_data['cost'])
      total_cost += item_cost

    # Now you have the total cost for all items
    request.session['order_total'] = str(total_cost)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required 
def manage_products(request):
    if request.user.is_superuser:
        get_products = Products.objects.all()
        product_form = ProductManagementForm()
        if request.method == 'POST':
            if request.POST['protein_source'] == "Yes":
                protein_source = True
            else:
                protein_source = False
            
            if request.POST['fibre_source'] == "Yes":
                fibre_source = True
            else:
                fibre_source = False
            try:
                add_item = Products(                
                product_placeholder_name = request.POST['product_placeholder_name'],
                product_name = request.POST['product_name'],
                product_price = Decimal(request.POST['product_price']),
                product_short_description = request.POST['product_short_description'],
                protein_source = protein_source,
                fibre_source = fibre_source,
                product_image_url =  request.POST['product_image_url'],
                category_id = 9,
                calorie_content = int(request.POST['calorie_content']),
                protein_content = Decimal(request.POST['protein_content']),
                fibre_content = Decimal(request.POST['fibre_content']),
                fat_content = Decimal(request.POST['fat_content']),
                saturated_fat_content = Decimal(request.POST['saturated_fat_content']),
                carbohydrate_content = Decimal(request.POST['carbohydrate_content']),
                carbohydrate_sugar_content = Decimal(request.POST['carbohydrate_sugar_content']),
                salt_content = Decimal(request.POST['salt_content']),
                )                            
                add_item.save()
                messages.success(request, 'Product created successfully!')
                return redirect(request.META.get('HTTP_REFERER'))
            except (ValueError, TypeError) as e:
                error_message = f'Error converting data: {str(e)}'
                return redirect(request.META.get('HTTP_REFERER'))    
        else:
            template = 'products/manage_products.html'
            context = {
                'get_products': get_products,                
                'product_form' : product_form,
            }
            return render(request, template, context)
    else:
        print("You do not have authoriation to access that page")
        return redirect(request.META.get('HTTP_REFERER'))




















def render_modification_form(request, product_id):
    if request.user.is_superuser:
        get_product = Products.objects.filter(product_id=product_id).first()
        if get_product:
            selected_pid = get_product.product_id
            product_data =  {
                'product_placeholder_name': get_product.product_placeholder_name,
                'product_short_description': get_product.product_short_description,
                'product_name': get_product.product_name,           
                'product_price': get_product.product_price,
                'protein_source': get_product.protein_source,
                'fibre_source': get_product.fibre_source,
                'product_image_url': get_product.product_image_url,
                'category_id': get_product.category_id,
                'calorie_content': get_product.calorie_content,
                'protein_content': get_product.protein_content,
                'fibre_content': get_product.fibre_content,
                'fat_content': get_product.fat_content,                        
                'saturated_fat_content': get_product.saturated_fat_content,            
                'carbohydrate_content': get_product.carbohydrate_content,
                'carbohydrate_sugar_content': get_product.carbohydrate_sugar_content,
                'salt_content': get_product.salt_content,
                }
            product_form = ProductManagementForm(product_data)
            template = 'products/modify_products.html'
            context = {
                    'product_data': product_data,
                    'product_form': product_form,
                    'selected_pid': selected_pid,
                }
            
            return render(request, template, context)
        else:
            print("No products found")
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        print("You do not have authorization to access that page")
        return redirect(request.META.get('HTTP_REFERER'))



MOFIDY IS NOT WORKING
FIX IT


def modify_product(request):
    if request.user.is_superuser:
        try:
            product_id = request.POST['selected_pid']          
            if request.POST['protein_source'] == "Yes":
                protein_source = True
            else:
                protein_source = False
            
            if request.POST['fibre_source'] == "Yes":
                fibre_source = True
            else:
                fibre_source = False            
            get_product = Products.objects.filter(product_id=product_id).first() 
            print(f"Type of price is {type(get_product['product_price'])}")       
            get_product.product_placeholder_name = request.POST['product_placeholder_name'],
            get_product.product_name = request.POST['product_name'],
            get_product.product_price = Decimal(request.POST['product_price']),
            get_product.product_short_description = request.POST['product_short_description'],
            get_product.protein_source = protein_source,
            get_product.fibre_source = fibre_source,
            get_product.product_image_url =  request.POST['product_image_url'],
            get_product.category_id = request.POST['category_id'],
            get_product.calorie_content = int(request.POST['calorie_content']),
            get_product.protein_content = Decimal(request.POST['protein_content']),
            get_product.fibre_content = Decimal(request.POST['fibre_content']),
            get_product.fat_content = Decimal(request.POST['fat_content']),
            get_product.saturated_fat_content = Decimal(request.POST['saturated_fat_content']),
            get_product.carbohydrate_content = Decimal(request.POST['carbohydrate_content']),
            get_product.carbohydrate_sugar_content = Decimal(request.POST['carbohydrate_sugar_content']),
            get_product.salt_content = Decimal(request.POST['salt_content']), 
            get_product.save()
            messages.success(request, 'Product modified successfully!')
            return redirect(request.META.get('HTTP_REFERER'))
        except (ValueError, TypeError) as e:
                error_message = f'Error converting data: {str(e)}'
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        print("You do not have authorization to access that page")
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



