

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('prepacked_sandwiches/', views.prepacked_sandwiches, name='prepacked_sandwiches'),
    path('sandwich_creator/', views.list_sandwich_creator_items, name='sandwich_creator'),
    #path('add_to_basket/', views.add_to_basket, name='add_to_basket'),          
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
