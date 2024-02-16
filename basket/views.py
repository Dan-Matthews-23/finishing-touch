from django.shortcuts import render

def basket(request):
    return render(request, 'basket/basket.html')


#def add_items_to_basket(request, product-id):
def add_items_to_basket(request, product_id):    

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if product_id in list(bag.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
    
# YOU NEED TO GO BACK THROUGH SCRIPT.JS AND SANDWICHES AND REPLACE ALL IDS WITH UNDERSCROLLS (_) 
# WHERE THERE ARE DASHES (-). aLSO CHECK STYLES. tHIS IS BECAUSE DASHES WILL NOT WORK WITH PYTHON