from django.db import transaction

from food_ordering.libs.redis.service import RedisPubSubService
from food_ordering.orders.models import Order, OrderFood


class OrderService:
    orders_created_channel_name = "orders.created"
    redis_pub_sub_service = RedisPubSubService(channel=orders_created_channel_name)

    @transaction.atomic()
    def create_order(self, user, restaurant, orderfood_set):
        order = Order.objects.create(user=user, restaurant=restaurant)

        orderfood_objs = [OrderFood(order=order, **orderfood) for orderfood in orderfood_set]
        OrderFood.objects.bulk_create(orderfood_objs)

        return order
