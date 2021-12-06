from rest_framework import generics, authentication, permissions
from rest_framework.permissions import AllowAny

from food_ordering.users.models import User
from food_ordering.users.serializers import UserSerializer, CreateUserSerializer


class ManageUserViewSet(generics.RetrieveUpdateAPIView):
    """
    Manage the authenticated user
    """

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserCreateViewSet(generics.CreateAPIView):
    """
    Create a new user in the system
    """

    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class UsersListAdminViewSet(generics.ListAPIView):
    """
    List all users in the system, requires Admin privilege
    """
    queryset = User.objects.order_by("-date_joined")
    permission_classes = (permissions.IsAdminUser,)
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = UserSerializer


class UserDetailAdminViewSet(generics.RetrieveAPIView):
    """
    Retrieve any user in the system, requires Admin privilege
    """
    queryset = User.objects.all()
    lookup_field = "id"
    permission_classes = (permissions.IsAdminUser,)
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = UserSerializer
