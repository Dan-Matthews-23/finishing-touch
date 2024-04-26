from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Orders, Reviews
from products.models import Products
from django.views.decorators.http import require_POST


@login_required
def update_profile(request):  
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

@login_required
def render_profile(request):  
    profile = get_object_or_404(UserProfile, user=request.user)    
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
        if reviews:            
            for review in reviews:            
                print(review.review_title, review.review_body, review.stars) 
            star_range = range(review.stars) 
        else: 
            star_range = range(1)  # Create a range even if no stars
    except Reviews.DoesNotExist:
        reviews = None 
    order_line_items = order.lineitems.all()     
    template = 'account/order_history.html'
    context = {
        'order': order,
        'star_range': star_range,
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
            messages.error(request,('Please fill out all fields'))
            return redirect(request.META.get('HTTP_REFERER'))      
        try:
            selected_rating = int(request.POST.get('selected_rating', 0))            
            review_title = request.POST.get('review_title')
            review_body = request.POST.get('review_body')           
            add_review = Reviews(order=order, stars=selected_rating, review_title=review_title, review_body=review_body) 
            add_review.save()  # Save the correct object             
        except:  
             messages.error(request,('There was an error prcocessing your review. Please try again in a few minutes'))
        return redirect(request.META.get('HTTP_REFERER'))