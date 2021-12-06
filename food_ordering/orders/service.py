from django.db import transaction

from food_ordering.orders.models import Order, OrderFood
from food_ordering.orders.pubsub import orders_pubsub_service


class OrderService:
    @staticmethod
    @transaction.atomic()
    def create_order(user, restaurant, orderfood_set):
        order = Order.objects.create(user=user, restaurant=restaurant)

        orderfood_objs = [OrderFood(order=order, **orderfood) for orderfood in orderfood_set]
        OrderFood.objects.bulk_create(orderfood_objs)

        # Publish order to pubsub channel
        OrderService.publish_order(order)

        return order

    @staticmethod
    def publish_order(order: Order):
        orders_pubsub_service.publish(str(order.uuid))
        order.status = Order.OrderStatus.WAITING
        order.save()

    @staticmethod
    def process_orders():
        orders_pubsub_service.process_subscribers()
