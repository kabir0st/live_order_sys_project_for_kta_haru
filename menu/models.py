from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

class CustomUser(AbstractUser):
	uuid = models.UUIDField(unique = True,default = uuid.uuid4)
	table_number = models.PositiveIntegerField(unique = True, null=True)

class FoodType(models.Model):
	food_type = models.CharField(max_length = 200,null = True)


class FoodItem(models.Model):
	name = models.CharField(max_length = 200)
	food_type = models.ForeignKey(FoodType, on_delete = models.CASCADE,null = True)
	price = models.PositiveIntegerField(default = 100)
	is_active = models.BooleanField(default= True)


class Order(models.Model):
	STATES = (
		('PAID', "Paid"),
		('PENDING', "Pending")
	)
	state = models.CharField(max_length=8, choices=STATES, default='PENDING')
	timestamp = models.DateTimeField(default=timezone.now)
	table_number = models.PositiveIntegerField(null = True)


class OrderedItem(models.Model):
	order = models.ForeignKey(Order,on_delete= models.CASCADE)
	food_item = models.ForeignKey(FoodItem, on_delete = models.CASCADE)


