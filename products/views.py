from django.shortcuts import render
from .models import Products, Category

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