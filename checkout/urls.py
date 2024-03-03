
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    #path('sandwich_creator/', views.list_sandwich_creator_items, name='sandwich_creator'),      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
