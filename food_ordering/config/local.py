from food_ordering.config.common import *

DEBUG = True

# Testing
INSTALLED_APPS += ("django_extensions",)

# Mail
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
