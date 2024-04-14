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
        if not request.POST.get('review_title') or not request.POST.get('review_body') or not request.POST.get('selected_rating', 0):
                messages.error(request,
                           ('Please fill out all fields'))
                return redirect(request.META.get('HTTP_REFERER'))      
        try:
            selected_rating = int(request.POST.get('selected_rating', 0))  # Get the rating
            #product_id = request.POST.get('product_id')
            review_title = request.POST.get('review_title')
            review_body = request.POST.get('review_body')
            #product = get_object_or_404(Products, pk=product_id)
            add_review = Reviews(order=order, stars=selected_rating, review_title=review_title, review_body=review_body) 
            add_review.save()  # Save the correct object 
            print(f"Your review was created")
        except Exception as e:  
            print(f"There was an error while saving your review: {e}")
        return redirect(request.META.get('HTTP_REFERER'))