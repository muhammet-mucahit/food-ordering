from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.update({"is_staff": False, "is_superuser": False})
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.update({"is_staff": True, "is_superuser": True})
        return self._create_user(email, password, **kwargs)
