
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('basket/', views.view_basket, name='view_basket'),
    #path('update_details/', views.update_details, name='update_details'),
    #path('sandwich_creator/', views.list_sandwich_creator_items, name='sandwich_creator'),      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 