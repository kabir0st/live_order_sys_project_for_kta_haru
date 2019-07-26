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
		Food = FoodItem.objects.all
		response_json = {'food_type':[], food:[]}
		# for ( f in Food):

		Foodtype = FoodType.objects.all
		return render(request, 'home.html', {'response_json': response_json})

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
