from django.shortcuts import render
from menu.models import Order, OrderedItem



def get_order(request):
    orders = Order.objects.all()
    response = {'order':[]}
    for order in orders:
        ordered_items = OrderedItem.objects.all().filter(order = order)
        json_order = {'name':[],'price':[]}
        for ordered_item in ordered_items:
            json_order['name'].append(ordered_item.food_item.name)
            json_order['price'].append(ordered_item.food_item.price)
        response['order'].append(json_order)
    print(response)
    return render(request, 'reception/reception.html', {'orders': response})


