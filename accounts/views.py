"""


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def showOrders(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    #user_details = {
        #'user': profile.user.username,  
        #'user' : profile.user,
        #'username': profile.user.username,
        #'default_phone_number': profile.default_phone_number,    
        #'default_postcode': profile.default_postcode,
        #'default_town_or_city': profile.default_town_or_city, 
        #'default_street_address1': profile.default_street_address1,
        #'default_street_address2': profile.default_street_address2,
        #'default_county': profile.default_county,   
        # 
        # #}
    orders = profile.orders.all()

    template = 'account/profile.html'
    context = { 
        #'user_details': user_details,    
        'orders': orders,
        'profile': profile,              
    }
    print(f"The order details is {profile}")
   

    return render(request, template, context)
"""

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Orders, Reviews
from products.models import Products


@login_required
def profile(request):  
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all().order_by('-date')

    template = 'account/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Orders, order_number=order_number)
    try:
        reviews = Reviews.objects.filter(order=order)
        print("Reviews found:", reviews)  # Print the queryset
        for review in reviews:            # Check individual review contents
            print(review.review_title, review.review_body, review.stars) 
    except Reviews.DoesNotExist:
        reviews = None  
        #print("No reviews found.") 

    # Get related order line items
    order_line_items = order.lineitems.all() 

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'account/order_history.html'
    context = {
        'order': order,
        'order_line_items': order_line_items,
        'reviews': reviews,
        'from_profile': True,
    }
    return render(request, template, context)






@login_required
def leave_review(request, order_number):
    if request.method == 'POST':
        order = get_object_or_404(Orders, order_number=order_number)
        for i in range(1, 6):
            if f"star_rating_{i}" in request.POST:
                selected_rating = i
                print(f"User selected a rating of {selected_rating} stars")                
                break          
        try:
            product_id = request.POST.get('product_id') 
            product = get_object_or_404(Products, pk=product_id)
            add_review = Reviews(order=order, stars=selected_rating, product=product) 
            add_review.save()  # Save the correct object 
            print(f"Your review was created")
        except Exception as e:  
            print(f"There was an error while saving your review: {e}")

        return redirect(request.META.get('HTTP_REFERER'))