from rest_framework import serializers

from food_ordering.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "auth_token",
        )
        read_only_fields = ("email", "auth_token",)


class CreateUserSerializer(UserSerializer):
    def create(self, validated_data):
        # call create_user on user object. Without this, the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            "password",
        )
        read_only_fields = ("auth_token",)
        extra_kwargs = {"password": {"write_only": True}}
