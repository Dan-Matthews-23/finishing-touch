from decimal import Decimal
from django.conf import settings

def basket_items(request):

    items = []
    price = 0
    quantity = 0

    # Add Delivery Things Here
    # https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/5ad560616d634896874fc24f20494e19/
      
    
    
    context = {
        'items': items,
        'price': price,
        'quantity': quantity,
        'total_price' : total_price,
        }

    return context