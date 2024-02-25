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

        # Process order items
        
        total_price = 0
        for i in range(0, len(order_items), 5):
            try:
                product_id = order_items[i]
                product_name = order_items[i + 1]
                default_price = order_items[i + 2]
                price = float(order_items[i + 3])
                product_quantity = order_items[i + 4] 
                price_calc = float(order_items[i + 5]) 

                item_total = price * product_quantity
                total_price += item_total  
            except IndexError:
                print(f"Missing default_price at index: {i}")         

        # Redirect to order confirmation or similar
            
            context = {
                'order_items': order_items,
                'total_price': total_price
            }
            #return redirect('basket', order_details)
            return render(request, 'basket/basket.html', context)
            
            #return redirect('basket')

    elif request.method == "GET":
        return render(request, 'basket/basket.html')










"""
#class process_order(forms.Form):
def process_order(request):  # Create a function to handle POST requests
    if request.method == "POST":            
            orderArrayData = request.POST.get("orderData")
            print(orderArrayData)
            order_items = json.loads(orderArrayData)
            total_price = 0
            for i in range(0, len(order_items), 6):
                product_id = order_items[i]
                product_name = order_items[i + 1]
                default_price = float(order_items[i + 2])
                price_calc = float(order_items[i + 3])                
                price = float(order_items[i + 4])
                product_quantity = order_items[i + 5]

                item_total = default_price * product_quantity
                total_price += item_total

            return redirect('basket', order_details={
            'order_items': order_items,
            'total_price': total_price
            })
    elif request.method == "GET":
        return render(request, 'basket/basket.html')





            #return render(request, 'basket/basket.html', product_id)
        #elif request.method == "GET":
            #return render(request, 'basket/basket.html')
        
        
    # Fields are: Product ID, product Name, default price, price calc, price, quantity    
                 
            
        
            

    # ... other methods if needed ... 


   """    



"""

def process_order(request):
    if request.method == 'POST':
        json_data = request.POST.get('orderData', '')  # Default to an empty string
        if json_data:
            python_data = json.loads(json_data)            
            for item in python_data:
                product_id = item['product_id']
                product_name = item['product_name']
                product_price = item['product_price']
                print(f"Product: {product_name} (ID: {product_id}) - Price: {product_price}")
            return render(request, 'basket/order_success.html')  # Example success page
        else:
            # Handle the case where jsonData is missing 
            return render(request, 'basket/error.html', {'error': 'Order data is missing'})
    else:
        return render(request, 'basket/basket.html')    
    
# FOR SOME REASON THE JSON STRING IS NOT BEING SUBMITTERD VIA POST. 
"""

"""    
def process_order(request):
    print(request.POST)  # Inspect the entire POST data
    if request.method == 'POST':
        return render(request, 'basket/basket.html') 
    return render(request, 'basket/basket.html') 
"""    


       


"""
def process_order(request):
    if request.method == 'POST':
        product_id = request.form.get("product_id");
        print(product_id);
        #request.session['orderData'] = request.POST.get('jsonData')
    # Assuming basket.html loads this view...
    #order_data = request.session.get('orderData') 
    return render(request, 'basket/basket.html', product_id) 
"""