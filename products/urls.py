

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('remove_item/', views.remove_item, name='remove_item'),
    path('prepacked_sandwiches/', views.prepacked_sandwiches, name='prepacked_sandwiches'),    
    path('add_to_favourites/', views.add_to_favourites, name='add_to_favourites'),          
    path('delete_from_favourites/', views.delete_from_favourites, name='delete_from_favourites'),
    path('add_to_order/', views.add_to_order, name='add_to_order'),
    path('clear_order/', views.clear_order, name='clear_order'),
    path('manage_products/', views.manage_products, name='manage_products'),
    path('render_modification_form/<product_id>/', views.render_modification_form, name='render_modification_form'),
    path('modify_product/', views.modify_product, name='modify_product'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
