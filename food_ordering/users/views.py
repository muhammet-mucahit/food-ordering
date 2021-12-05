from rest_framework import generics
from rest_framework.permissions import AllowAny
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
