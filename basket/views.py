from django.shortcuts import render
from .models import Basket
import json

# Create your views here.

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
    
def process_order(request):
    if request.method == 'POST':
        request.session['orderData'] = request.POST.get('jsonData')
    # Assuming basket.html loads this view...
    order_data = request.session.get('orderData') 
    return render(request, 'basket/basket.html', {'order_data': order_data}) 
