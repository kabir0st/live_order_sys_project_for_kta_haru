from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

class CustomUser(AbstractUser):
	uuid = models.UUIDField(unique = True,default = uuid.uuid4)
	is_manager = models.BooleanField(default= False)
	is_reception = models.BooleanField(default= True)
	passcode = models.IntegerField(default= 666)

	def __str__(self):
		return str(self.first_name)


class FoodType(models.Model):
	food_type = models.CharField(max_length = 200,null = True)

	def __str__(self):
		return str(self.food_type)

class Table(models.Model):
	table_number = models.PositiveIntegerField(unique = True, null=True)
	uuid = models.UUIDField(unique = True,default = uuid.uuid4)
	
	def __str__(self):
		return str(self.table_number)


class FoodItem(models.Model):
	name = models.CharField(max_length = 200)
	food_type = models.ForeignKey(FoodType, on_delete = models.CASCADE,null = True)
	price = models.PositiveIntegerField(default = 100)
	is_active = models.BooleanField(default= True)

	def __str__(self):
		return str(self.name)

class Order(models.Model):
	is_done = models.BooleanField(default=False)
	timestamp = models.DateTimeField(default=timezone.now)
	table_number = models.ForeignKey(Table, blank = True, null = True, on_delete = models.SET_NULL)

	def __str__(self):
		return str(self.timestamp)
	

class OrderedItem(models.Model):
	order = models.ForeignKey(Order,on_delete= models.CASCADE)
	food_item = models.ForeignKey(FoodItem, on_delete = models.CASCADE)

	def __str__(self):
		return str(self.food_item)
	
