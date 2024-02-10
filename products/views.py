from django.shortcuts import render
from .models import Products

# Create your views here.

def list_all_products(request):
    products = Products.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'products/products.html', context)