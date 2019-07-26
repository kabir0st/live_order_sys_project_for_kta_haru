from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

class CustomUser(AbstractUser):
	uuid = models.UUIDField(unique = True,default = uuid.uuid4)
	table_number = models.PositiveIntegerField(unique = True, null=True)

	def __str__(self):
		return str(self.table_number)


class FoodType(models.Model):
	food_type = models.CharField(max_length = 200,null = True)

	def __str__(self):
		return str(self.food_type)


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
	table_number = models.ForeignKey(CustomUser, blank = True, null = True, on_delete = models.SET_NULL)

	def __str__(self):
		return str(self.timestamp)
	

class OrderedItem(models.Model):
	order = models.ForeignKey(Order,on_delete= models.CASCADE)
	food_item = models.ForeignKey(FoodItem, on_delete = models.CASCADE)

	def __str__(self):
		return str(self.food_item)
	
