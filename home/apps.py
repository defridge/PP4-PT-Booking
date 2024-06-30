from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration for the home application

    Attributes:
        default_auto_field (str): The default primary key field type
        name (str): The name of the application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
