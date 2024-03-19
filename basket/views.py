from django.shortcuts import render, redirect
from .models import Basket
import json
from django import forms
import uuid



# Create your views here.

"""
('[{"product_id":"6","product_name":"Egg Mayonnaise","default_price":2.4,"price":"2.40","product_quantity":1,"price_calc":2.4}]') 
"""

def basket(request, context):
    return render(request, 'basket/basket.html')




def process_order(request):
    if request.method == "POST":
        orderArrayData = request.POST.get("orderData")
        order_items = json.loads(orderArrayData)
        total_price = 0
        order_number = uuid.uuid4() 

        for item in order_items:
            try:
                default_price = float(item['default_price'])              
                quantity = item['product_quantity']
                
                total_price = float(total_price)
                total_price += default_price * quantity
                total_price = f"{total_price:.2f}"

                create_basket_item = Basket.objects.create(
                    order_number = order_number,
                    product_id = item['product_id'],
                    quantity = item['product_quantity'],
                    default_price = item['default_price'],
                    sub_price = item['price'],
                    product_name = item['product_name'],
                    
                    ) 
                create_basket_item.save()           
                

            except KeyError as e:
                print(f"Missing key '{e}' in order item: {item}")

        context = {
            'order_items': order_items,
            'total_price': total_price,
            
        }
       
        request.session['order_number'] =str(order_number)
        request.session['basket'] = order_items
        request.session['total_price'] = total_price
        #print(f" The type of session is {type(request.session['total_price'])} and the value is {request.session['total_price']}")
        return render(request, 'basket/basket.html', context)
        

    elif request.method == "GET":
        return render(request, 'basket/basket.html')











"""

 product_id_from_array = item['product_id']
                print(f"The type of product_id_from_array is {type(product_id_from_array)} and its value is {product_id_from_array}")

                product_name_from_array = item['product_name']
                print(f"The type of product_name_from_array is {type(product_name_from_array)} and its value is {product_name_from_array}")

                default_price_from_array = item['default_price']                
                print(f"The type of default_price_from_array is {type(default_price_from_array)} and its value is {default_price_from_array}")
                
                product_quantity_from_array = item['product_quantity']
                print(f"The type of product_quantity_from_array is {type(product_quantity_from_array)} and its value is {product_quantity_from_array}")

                price_from_array = item['price']
                print(f"The type of price_from_array is {type(price_from_array)} and its value is {price_from_array}")      

                """