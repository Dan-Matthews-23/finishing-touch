from django.shortcuts import render
from django.http import JsonResponse  # For sending JSON responses
from django.shortcuts import render
import json

def basket(request):
    return render(request, 'basket/basket.html')




def process_order(request):
    if request.method == 'POST':
        order_data = request.POST.get('orderData')  
        order_array = json.loads(order_data)

        # Process the order_array in Django
        # ...

        return JsonResponse({'status': 'success'}) # Return success response
    else:
        # Handle other request methods if needed
        return render(request, 'error_page.html')  # Example error handling
