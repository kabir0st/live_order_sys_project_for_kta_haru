from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodType, FoodItem, Order, OrderedItem, CustomUser
import json

def home(request):
	if request.method == "POST":
		json_str = request.body.decode(encoding= 'UTF-8')
		data = json.loads(json_str)
		names = data['name']
		prices = data['price']
		ids = data['id']
		for i in range(len(names)):
			order = Order.objects.create(item_id = ids[i], item_name = names[i], price = prices[i])
			order.save()


		return HttpResponse("Ordered vayo vai")
	else:
		Food = FoodItem.objects.all
		Foodtype = FoodType.objects.all
		return render(request, 'home.html', {'Food': Food, 'Foodtype': Foodtype})