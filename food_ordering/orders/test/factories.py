import factory.fuzzy

from food_ordering.orders.models import Order
from food_ordering.restaurants.test.factories import RestaurantFactory, FoodFactory
from food_ordering.users.test.factories import UserFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "orders.Order"

    uuid = factory.Faker("uuid4")
    restaurant = factory.SubFactory(RestaurantFactory)
    user = factory.SubFactory(UserFactory)
    status = factory.fuzzy.FuzzyChoice(Order.OrderStatus)


class OrderFoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "orders.OrderFood"

    order = factory.SubFactory(OrderFactory)
    food = factory.SubFactory(FoodFactory)
    quantity = factory.fuzzy.FuzzyInteger(low=0, high=10)
