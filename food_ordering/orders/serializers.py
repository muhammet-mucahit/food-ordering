from rest_framework import serializers

from food_ordering.orders.models import Order, OrderFood


class OrderFoodCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = (
            "food",
            "quantity",
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    orderfood_set = OrderFoodCreateSerializer(
        many=True,
        required=True,
        allow_empty=False,
        help_text="""[
                {"food": 5, "quantity": 3},
                {"food": 1, "quantity": 5},
                ...
            """,
    )

    class Meta:
        model = Order
        fields = ("id", "restaurant", "orderfood_set")
        read_only_fields = ("id",)

    def validate(self, attrs):
        restaurant = attrs["restaurant"]
        orderfood_set = attrs["orderfood_set"]

        if not all(restaurant == orderfood["food"].restaurant for orderfood in orderfood_set):
            raise serializers.ValidationError("You are trying to order some foods which don't exist in the restaurant")

        return attrs
