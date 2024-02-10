from django.shortcuts import render
from .models import Products

# Create your views here.

# Display all breads
def list_all_breads(request):
    #products = Products.objects.all()
    breads = Products.objects.filter(category_id=1)
    context = {
        'breads' : breads,
    }
    return render(request, 'products/products.html', context)

# Display all fillings
def list_all_fillings(request):    
    fillings = Products.objects.filter(category_id=2)
    context = {
        'fillings' : fillings,
    }
    return render(request, 'products/products.html', context)