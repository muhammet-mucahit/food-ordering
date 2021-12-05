from django.contrib import admin

from food_ordering.restaurants.models import Food, Restaurant, RestaurantCategory

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(RestaurantCategory)
