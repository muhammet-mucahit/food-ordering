from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("food_ordering.users.urls")),
    path("api/v1/orders/", include("food_ordering.orders.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
