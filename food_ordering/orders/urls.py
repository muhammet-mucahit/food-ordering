from django.urls import path

from food_ordering.orders.views import OrderCreateViewSet, order_process_view, OrderListViewSet

app_name = "orders"

urlpatterns = [
    path("", OrderCreateViewSet.as_view(), name="create"),
    path("process/", order_process_view, name="process"),
    path("list/", OrderListViewSet.as_view(), name="list"),
]
