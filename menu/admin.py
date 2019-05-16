from django.contrib import admin
from .models import FoodItem, Order, OrderedItem, CustomUser, FoodType

admin.site.register(FoodItem)

admin.site.register(FoodType)

admin.site.register(Order)

admin.site.register(OrderedItem)

admin.site.register(CustomUser)
