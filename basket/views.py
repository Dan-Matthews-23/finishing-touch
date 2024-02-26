from django.shortcuts import render, redirect
from .models import Basket
import json
from django import forms


# Create your views here.

"""
('[{"product_id":"6","product_name":"Egg Mayonnaise","default_price":2.4,"price":"2.40","product_quantity":1,"price_calc":2.4}]')
"""

def basket(request, context):
    return render(request, 'basket/basket.html')




def process_order(request):
    if request.method == "POST":
        orderArrayData = request.POST.get("orderData")
        print(orderArrayData)
        order_items = json.loads(orderArrayData) 
        total_price = 0
        for item in order_items:
            try:
                product_id = item['product_id']

                product_name = item['product_name']
                
                default_price = round(float(item['default_price']), 2)
                print(f"The type of default_price is {type(default_price)}")

                                
                product_quantity = item['product_quantity']
                print(f"The type of quantity is {type(product_quantity)}")

                price_calc = round(float(item['price_calc']), 2)
                print(f"The type of price_calc is {type(price_calc)}")


                for item in order_items:
                    total_price += round(float(item['default_price']), 2) * item['product_quantity']
                    print(f"The type of total_price is {type(total_price)}")   
                                   
                          
            except KeyError as e:
                print(f"Missing key '{e}' in order item: {item}")            
            context = {
                'order_items': order_items,
                'total_price': round(float(total_price), 2)
            }
            #return redirect('basket', order_details)
            return render(request, 'basket/basket.html', context)
    elif request.method == "GET":
        return render(request, 'basket/basket.html')












