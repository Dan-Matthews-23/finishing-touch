from django.shortcuts import render
from .models import Products

# Create your views here.

# Display all breads
def list_all_sandwitch_items(request):   
    sandwitch_items = Products.objects.all()
    context = {
        'sandwitch_items' : sandwitch_items,
    }
    return render(request, 'products/products.html', context)



