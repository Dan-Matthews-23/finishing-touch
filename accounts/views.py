from django.shortcuts import render






def showOrders(request):
    

    template = 'account/profile.html'
    context = {       
                
               
    }
   

    return render(request, template, context)
