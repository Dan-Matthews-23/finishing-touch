
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.checkout, name='checkout'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('create_placeholder/', views.create_placeholder, name='create_placeholder'),      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)