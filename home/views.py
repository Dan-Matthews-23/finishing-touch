from django.shortcuts import render
from products.models import Products, Category


def home(request):
    sandwich_items = Products.objects.all()
    context = {
        'sandwich_items': sandwich_items,
    }
    return render(request, 'home/index.html', context)
