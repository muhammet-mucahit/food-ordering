import factory.fuzzy


class RestaurantCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "restaurants.RestaurantCategory"
        django_get_or_create = ("name",)

    name = factory.Faker("name")


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "restaurants.Restaurant"

    name = factory.Faker("name")
    category = factory.SubFactory(RestaurantCategoryFactory)
    is_active = True


class FoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "restaurants.Food"

    name = factory.Faker("name")
    restaurant = factory.SubFactory(RestaurantFactory)
    price = factory.fuzzy.FuzzyDecimal(low=0.0, high=100.0)
    is_active = True
