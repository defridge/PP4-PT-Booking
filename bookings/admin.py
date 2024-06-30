from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Booking model

    Attributes:
        list_display (tuple): Fields to display in the admin list view
        list_filter (tuple): Fields to filter the admin list view by
    """
    list_display = (
        'user', 'session_type', 'date', 'time',
        'contact_number', 'contact_email')
    list_filter = ('date', 'time', 'session_type')


admin.site.register(Booking, BookingAdmin)
