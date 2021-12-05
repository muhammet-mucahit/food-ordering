import uuid

from django.db import models
from django.utils.functional import cached_property

from food_ordering.core.models import BaseModel
from food_ordering.restaurants.models import Restaurant, Food
from food_ordering.users.models import User


class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        CREATED = "CREATED"
        WAITING = "WAITING"
        COMPLETED = "COMPLETED"
        REJECTED = "REJECTED"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=64, choices=OrderStatus.choices, default=OrderStatus.CREATED, db_index=True)

    @cached_property
    def total_price(self):
        return sum(order_food.price for order_food in self.orderfood_set.all())


class OrderFood(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    @cached_property
    def price(self):
        return self.food.price * self.quantity
