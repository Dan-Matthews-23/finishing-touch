from django.shortcuts import render






def showOrders(request):
    

    template = 'accounts/profile.html'
    context = {       
                
               
    }
   

    return render(request, template, context)
