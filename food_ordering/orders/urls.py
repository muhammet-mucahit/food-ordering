from django.urls import path

from food_ordering.orders.views import OrderCreateViewSet

app_name = "orders"

urlpatterns = [
    path("", OrderCreateViewSet.as_view(), name="create"),
]
