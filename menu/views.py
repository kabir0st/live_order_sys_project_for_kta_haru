from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodType, FoodItem, Order, OrderedItem, CustomUser
import json

def home(request):
	if request.method == "POST":
		json_str = request.body.decode(encoding= 'UTF-8')
		data = json.loads(json_str)
		names = data['name']
		order = Order.objects.create()
		for i in range(len(names)):
			item = FoodItem.objects.get(name = names[i])
			order_items = OrderedItem.objects.create(order = order, food_item = item)
			order_items.save()
		return HttpResponse("Ordered vayo vai")
	else:
		Food = FoodItem.objects.all
		Foodtype = FoodType.objects.all
		return render(request, 'home.html', {'Food': Food, 'Foodtype': Foodtype})

