from django.http import JsonResponse
from rest_framework import generics, permissions, authentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from food_ordering.orders.models import Order
from food_ordering.orders.serializers import OrderCreateSerializer, OrderSerializer
from food_ordering.orders.service import OrderService


class OrderCreateViewSet(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        order = OrderService.create_order(user=self.request.user, **serializer.validated_data)
        serializer.instance = order


class OrderListViewSet(generics.ListAPIView):
    queryset = Order.objects.order_by("-modified_date")
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAdminUser,)
    filterset_fields = ["status"]


@api_view(http_method_names=["POST"])
@authentication_classes(authentication_classes=(authentication.TokenAuthentication,))
@permission_classes(permission_classes=(permissions.IsAdminUser,))
def order_process_view(request):
    OrderService.process_orders()
    return JsonResponse({"message": "Orders processed successfully"})
