

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('prepacked_sandwiches/', views.prepacked_sandwiches, name='prepacked_sandwiches'),    
    path('add_to_favourites/', views.add_to_favourites, name='add_to_favourites'),          
    #path('display_favourites/', views.display_favourites, name='display_favourites'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
