from rest_framework import generics

from food_ordering.orders.serializers import OrderCreateSerializer
from food_ordering.orders.service import OrderService


class OrderCreateViewSet(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    service = OrderService()

    def perform_create(self, serializer):
        order = self.service.create_order(user=self.request.user, **serializer.validated_data)
        serializer.instance = order
