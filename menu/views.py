from django.shortcuts import render
from .models import Menu

def home(request):
	all_items= Menu.objects.all
	return render(request, 'home.html', {'all_items': all_items})