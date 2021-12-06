from django.test import TestCase

from food_ordering.orders.test.factories import OrderFactory


class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = OrderFactory.create()

    def test_total_price_is_correct(self):
        orderfood_set = self.order.orderfood_set.all()
        total_price = sum(orderfood.food.price * orderfood.quantity for orderfood in orderfood_set)
        self.assertEqual(self.order.total_price, total_price)
