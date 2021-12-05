from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

from food_ordering.orders.models import Order
from food_ordering.restaurants.test.factories import FoodFactory, RestaurantFactory
from food_ordering.users.models import User

fake = Faker()


class OrderCreateViewSetTestCase(APITestCase):
    """
    Tests /orders create operations.
    """

    def setUp(self):
        self.url = reverse("orders:create")

        self.customer = User.objects.create_user("mucahitaktepe@gmail.com")

        self.food_1 = FoodFactory.create()
        self.food_2 = FoodFactory.create()

        self.client.force_authenticate(self.customer)

    def test_only_authenticated_users_can_access(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        order_data = {
            "restaurant": self.food_1.restaurant.id,
            "orderfood_set": [{"food": self.food_1.id, "quantity": 3}],
        }

        response = self.client.post(self.url, order_data, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        order = Order.objects.get(pk=response.data.get("id"))
        self.assertEquals(order.user, self.customer)
        self.assertEquals(order.restaurant.id, order_data["restaurant"])
        self.assertEquals(order.orderfood_set.count(), 1)

        order_food = order.orderfood_set.get()
        self.assertEquals(order_food.price, order.total_price)

    def test_creating_order_with_non_existing_food(self):
        order_data = {
            "restaurant": self.food_1.restaurant.id,
            "orderfood_set": [{"food": -1, "quantity": 3}],  # non exist food_id
        }
        response = self.client.post(self.url, order_data, format="json")
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("orderfood_set", str(response.content))

    def test_creating_order_with_non_existing_food_in_given_restaurant(self):
        restaurant1 = RestaurantFactory.create()
        restaurant2 = RestaurantFactory.create()

        self.food_1.restaurant = restaurant1
        self.food_1.save()

        self.food_2.restaurant = restaurant2
        self.food_2.save()

        order_data = {
            "restaurant": restaurant1.id,
            "orderfood_set": [
                {"food": self.food_2.id, "quantity": 3}  # The food_2 is not exist in food_1's restaurant
            ],
        }
        response = self.client.post(self.url, order_data, format="json")
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", str(response.content))

    def test_other_methods_not_available(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.url)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
