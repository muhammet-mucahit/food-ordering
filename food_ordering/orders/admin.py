from django.contrib import admin

from food_ordering.orders.models import Order, OrderFood

admin.site.register(Order)
admin.site.register(OrderFood)
