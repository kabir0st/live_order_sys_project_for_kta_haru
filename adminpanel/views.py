from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
def adminpanel(request):
    return render(request, 'adminpanel.html')