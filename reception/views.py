from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from menu.models import Order, OrderedItem



def get_order(request):
    orders = Order.objects.all()
    response = {'order':[]}
    for order in orders:
        json_order = {'name':[],'price':[],'id':int(order.id)}
        json_order['table_number'] = str(order.table_number)
        if not order.is_done:     
            ordered_items = OrderedItem.objects.all().filter(order = order)
            for ordered_item in ordered_items:
                json_order['name'].append(ordered_item.food_item.name)
                json_order['price'].append(ordered_item.food_item.price)
            response['order'].append(json_order)
    return render(request, 'reception/reception.html', {'orders': response})

def order_done(request,id):
    order = Order.objects.get(id=id)
    order.is_done = True
    order.save()
    return HttpResponseRedirect("/reception")



