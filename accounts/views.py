from django.shortcuts import render

def showOrders(request, context):
    return render(request, 'accounts/account.html')
