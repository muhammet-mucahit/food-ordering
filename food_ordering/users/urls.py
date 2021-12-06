from django.urls import path

from food_ordering.users.views import UserCreateViewSet, ManageUserViewSet, UserDetailAdminViewSet, \
    UsersListAdminViewSet

app_name = "users"

urlpatterns = [
    path("", UserCreateViewSet.as_view(), name="create"),
    path("me/", ManageUserViewSet.as_view(), name="me"),
    path("list/", UsersListAdminViewSet.as_view(), name="list"),
    path("<uuid:id>/", UserDetailAdminViewSet.as_view(), name="retrieve"),
]
