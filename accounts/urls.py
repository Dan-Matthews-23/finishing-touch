
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .webhooks import webhook


urlpatterns = [
    path('', views.showOrders, name='showOrders'),
    
    


] 


