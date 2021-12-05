from django.db import models

from food_ordering.core.models import BaseModel


class RestaurantCategory(BaseModel):
    name = models.CharField(max_length=64, unique=True)


class Restaurant(BaseModel):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(RestaurantCategory, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)


class Food(BaseModel):
    name = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
