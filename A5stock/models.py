from django.db import models

class PizzaStock(models.Model):
    pizza_name=models.CharField(max_length=100)
    pizza_price=models.IntegerField()
    pizza_type=models.CharField(max_length=130)
    pizza_size=models.CharField(max_length=50)
    quantity=models.IntegerField()
    def __str__(self):
        return self.pizza_name
# Create your models here.
