from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodType, FoodItem, Order, OrderedItem, CustomUser, Table
import json

def home(request,table_number):
	if request.method == "POST":
		json_str = request.body.decode(encoding= 'UTF-8')
		data = json.loads(json_str)
		names = data['name']
		table = Table.objects.get(table_number = int(table_number))
		order = Order.objects.create(table_number = table)
		for i in range(len(names)):
			item = FoodItem.objects.get(name = names[i])
			order_items = OrderedItem.objects.create(order = order, food_item = item)
			order_items.save()
		return HttpResponse("Ordered vayo vai")
	else:
		return render(request, 'home.html')


def get_menu(request):
	Food = FoodItem.objects.all()
	food_list = {}
	Foodtype = FoodType.objects.all()
	for typename in Foodtype:
		food_list[str(typename.food_type)] = {'name':[], 'price':[]}
	print(food_list)
	for f in Food :
		if(f.is_active):
			food_list[str(f.food_type)]['name'].append(str(f.name))
			food_list[str(f.food_type)]['price'].append(str(f.price))
	print(food_list)
	return HttpResponse(json.dumps(food_list), content_type = 'application/json')	


def login_user(request):
	if request.method == "POST":
		json_str = request.body.decode(encoding= 'UTF-8')
		data = json.loads(json_str)
		uuid = data['uuid']
		print(uuid)
		table = Table.objects.get(uuid = uuid)
		print(int(table.table_number))
		return HttpResponse(int(table.table_number))
	return render(request, 'login.html')
