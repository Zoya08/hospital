# The `UserConfig` class in Django specifies the default auto field and the name of the app.
from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
