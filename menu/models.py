from django.db import models

class Menu(models.Model):
	item_id = models.IntegerField()
	item_name = models.CharField(max_length=50)
	price = models.FloatField(max_length=50)

	def __str__(self):
		return self.item_name + ' - ' + str(self.price)

class Order(models.Model):
	item_id = models.IntegerField()
	item_name = models.CharField(max_length=50)
	price = models.FloatField(max_length=50)
	
	def __str__(self):
		return self.item_name + ' - ' + str(self.price)
