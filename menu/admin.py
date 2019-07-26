from django.contrib import admin
from .models import FoodItem, Order, OrderedItem, CustomUser, FoodType, Table

admin.site.register(FoodItem)

admin.site.register(FoodType)

admin.site.register(Order)

admin.site.register(OrderedItem)

admin.site.register(CustomUser)

admin.site.register(Table)
