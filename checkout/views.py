from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

import stripe

def checkout(request):
    return render(request, 'home/index.html')



def process_checkout(request):
    #basket = request.session.get()('basket', {})
    #if not basket:
        #messages.error(request, 'There is nothing in your bag')
        #return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key' : 'pk_test_51OqHDoJECgN7JZCtAwNm2Vjb1Hvfn7EVKPwVFmsV7LCOJSolHJuAuYE4SfBAIoDgDkb98DVRVRm2L7dQRgpUotrR00gaa7Vnmp',
        'client_secret' : 'test client secret',
    }

    return render(request, template, context)




