from food_ordering.libs.redis.service import Publisher, Subscriber, PubSubService
from food_ordering.orders.models import Order

orders_created_channel = "orders.created"
orders_publisher = Publisher(channel=orders_created_channel)


def accept_order(order_uuid):
    order = Order.objects.get(uuid=order_uuid)
    order.status = Order.OrderStatus.ACCEPTED
    order.save()


def email_user(order_uuid):
    order = Order.objects.get(uuid=order_uuid)
    order.notify_about_accepted_order()


accept_order_subscriber = Subscriber(channel=orders_created_channel, callback=accept_order)
email_user_about_accepted_order_subscriber = Subscriber(channel=orders_created_channel, callback=email_user)
orders_subscribers = [
    accept_order_subscriber,
    email_user_about_accepted_order_subscriber
]
orders_pubsub_service = PubSubService(orders_publisher, orders_subscribers)
