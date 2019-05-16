from django.db import models

class Menu(models.Model):
	food_item = models.CharField(max_length=50)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.item_name + ' - ' + str(self.price)

class Order(models.Model):
	table = models.ForeignKey(User,on_delete=models.CASCADE)
	food_item = models.CharField(max_length=50)
	Total_price = models.IntegerField()

	def __str__(self):
		return self.item_name + ' - ' + str(self.price)

