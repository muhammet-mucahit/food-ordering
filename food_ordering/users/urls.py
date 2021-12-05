from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from food_ordering.users.views import UserCreateViewSet, ManageUserViewSet

app_name = "users"

urlpatterns = [
    path("", UserCreateViewSet.as_view(), name="create"),
    path("me/", ManageUserViewSet.as_view(), name="me"),
    path("obtain_token/", obtain_auth_token),
]
