from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestUserManager(TestCase):
    def test_create_user(self):
        email = "example@example.com"
        kwargs = {"first_name": "Example First Name"}
        user = User.objects.create_user(email=email, **kwargs)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, kwargs["first_name"])
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_user_super_permissions_always_false(self):
        email = "example@example.com"
        permission_data = {"is_staff": True, "is_superuser": True}
        user = User.objects.create_user(email=email, **permission_data)
        self.assertEqual(user.email, email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        email = "example@example.com"
        user = User.objects.create_superuser(email=email)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_super_user_super_permissions_always_true(self):
        email = "example@example.com"
        permission_data = {"is_staff": False, "is_superuser": False}
        user = User.objects.create_superuser(email=email, **permission_data)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
