from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """
    Configuration for the bookings application

    Attributes:
        default_auto_field (str): The default primary key field type
        name (str): The name of the application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
