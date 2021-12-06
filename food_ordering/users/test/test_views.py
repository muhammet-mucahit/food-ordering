from django.urls import reverse
from django.contrib.auth.hashers import check_password
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory

from food_ordering.users.models import User
from food_ordering.users.test.factories import UserFactory

fake = Faker()


class UserCreateViewSetTestCase(APITestCase):
    """
    Tests /users create operations.
    """

    def setUp(self):
        self.url = reverse("users:create")
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.user_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(pk=response.data.get("id"))
        self.assertEquals(user.email, self.user_data.get("email"))
        self.assertTrue(check_password(self.user_data.get("password"), user.password))

    def test_other_methods_not_available(self):
        response = self.client.get(self.url, self.user_data)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.url, self.user_data)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url, self.user_data)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class ManageUserViewSetTestCase(APITestCase):
    """
    Tests /users/me detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse("users:me")
        self.client.force_authenticate(self.user)

    def test_only_authenticated_users_can_access(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_put_request_updates_a_user(self):
        new_first_name = fake.first_name()
        payload = {"first_name": new_first_name}
        response = self.client.put(self.url, payload)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(pk=self.user.id)
        self.assertEquals(user.first_name, new_first_name)

    def test_patch_request_updates_a_user(self):
        new_last_name = fake.last_name()
        payload = {"last_name": new_last_name}
        response = self.client.patch(self.url, payload)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(pk=self.user.id)
        self.assertEquals(user.last_name, new_last_name)

    def test_read_only_fields_cannot_be_updated(self):
        new_auth_token = fake.word()
        payload = {"auth_token": new_auth_token}
        response = self.client.patch(self.url, payload)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(pk=self.user.id)
        self.assertNotEquals(user.auth_token, new_auth_token)

    def test_email_cannot_be_updated(self):
        new_email = fake.email()
        payload = {"email": new_email}
        response = self.client.patch(self.url, payload)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(pk=self.user.id)
        self.assertNotEquals(user.email, new_email)

    def test_post_method_not_available(self):
        response = self.client.post(self.url, {})
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class UserDetailAdminViewSetTestCase(APITestCase):
    """
    Tests /users/<uuid:id> retrieve operations.
    """

    def setUp(self):
        self.user = UserFactory.create()
        self.admin_user = UserFactory.create(is_staff=True)
        self.url = reverse("users:retrieve", args=(self.user.id,))

    def test_that_requires_admin_privilege(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_no_data_fails(self):
        self.client.force_authenticate(self.admin_user)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(self.user.email, response.data["email"])
