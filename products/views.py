from django.shortcuts import render
from .models import Products, Category
import json

# Create your views here.

# Display all breads
def prepacked_sandwiches(request):   
    sandwich_items = Products.objects.all()
    context = {
        'sandwich_items' : sandwich_items,
    }
    return render(request, 'products/sandwiches.html', context)



def list_sandwich_creator_items(request):   
    sandwich_items = Products.objects.all() # Remove the filter once you get this working
    context = {
        'sandwich_items' : sandwich_items,
    }
    return render(request, 'products/sandwich-creator.html', context) 


def add_to_basket(request):
    if request.method == "POST":
        orderArrayData = request.POST.get("orderData")
        order_items = json.loads(orderArrayData)
        total_price = 0

        for item in order_items:
            try:
                default_price = float(item['default_price'])              
                quantity = item['product_quantity']
                
                total_price = float(total_price)
                total_price += default_price * quantity
                total_price = f"{total_price:.2f}"              
                

            except KeyError as e:
                print(f"Missing key '{e}' in order item: {item}")

        context = {
            'order_items': order_items,
            'total_price': total_price
        }
        request.session['basket'] = context
        print(request.session['basket'])
        return render(request, 'basket/basket.html', context)

    elif request.method == "GET":
        return render(request, 'basket/basket.html')