from django.core.management.base import BaseCommand

from food_ordering.users.test.factories import UserFactory

from food_ordering.restaurants.test.factories import RestaurantFactory, RestaurantCategoryFactory, FoodFactory


# TODO: TEST THIS COMMAND
class Command(BaseCommand):
    """Django command to initialize data with examples"""

    def handle(self, *args, **options):
        self.stdout.write("Initializing data...")

        UserFactory.create(email="uozy@ypst.com", first_name="Uğur", last_name="Özi")

        category_doner_kebap = RestaurantCategoryFactory.create(name="Döner/Kebap")
        category_ev_yemekleri = RestaurantCategoryFactory.create(name="Ev Yemekleri")
        category_fast_food = RestaurantCategoryFactory.create(name="Fast-Food")

        restaurant_super_donerci = RestaurantFactory.create(name="Süper Dönerci", category=category_doner_kebap)
        restaurant_harika_ev_yemekleri = RestaurantFactory.create(
            name="Harika Ev Yemekleri", category=category_ev_yemekleri
        )
        restaurant_bizim_bufe = RestaurantFactory.create(name="Bizim Büfe", category=category_fast_food)

        # Foods for Super Dönerci
        FoodFactory.create(name="Döner", restaurant=restaurant_super_donerci)
        FoodFactory.create(name="İskender", restaurant=restaurant_super_donerci)
        FoodFactory.create(name="Etibol İskender", restaurant=restaurant_super_donerci)

        # Foods for Harika Ev Yemekleri
        FoodFactory.create(name="Kuru Fasulye", restaurant=restaurant_harika_ev_yemekleri)
        FoodFactory.create(name="Pilav", restaurant=restaurant_harika_ev_yemekleri)
        FoodFactory.create(name="Mercimek Çorbası", restaurant=restaurant_harika_ev_yemekleri)

        # Foods for Bizim Büfe
        FoodFactory.create(name="Goralı", restaurant=restaurant_bizim_bufe)
        FoodFactory.create(name="Dilli Kaşarlı", restaurant=restaurant_bizim_bufe)
        FoodFactory.create(name="Yengen", restaurant=restaurant_bizim_bufe)

        self.stdout.write(self.style.SUCCESS("Database was filled with example data 🏆"))
