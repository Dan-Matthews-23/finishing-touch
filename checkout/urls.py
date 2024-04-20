
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .webhooks import webhook

urlpatterns = [
    path('process_checkout/', views.process_checkout, name='process_checkout'),    
    #path('', views.render_basket_form, name='render_basket_form'),
    #path('process_order/', views.process_order, name='process_order'),
    #path('create_payment/', views.create_payment, name='create_payment'),
    #path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    #path('create_placeholder/', views.create_placeholder, name='create_placeholder'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('order_confirmed/', views.checkout_success, name='checkout_success'),
    


] 


