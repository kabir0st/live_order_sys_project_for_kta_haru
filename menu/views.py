from django.shortcuts import render
from .models import Menu
import json

def home(request):
	if request.method == "POST":
		json_str = request.body.decode(encoding= 'UTF-8')
		print(json_str)
	else:
		all_items= Menu.objects.all
		return render(request, 'home.html', {'all_items': all_items})