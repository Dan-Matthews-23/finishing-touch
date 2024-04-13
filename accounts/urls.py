
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .webhooks import webhook


urlpatterns = [
    #path('', views.showOrders, name='showOrders'),
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('order_history/<order_number>/rate',
         views.leave_review,
         name='leave_review'),

] 


