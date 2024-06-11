from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_type', 'date', 'time', 'contact_number', 'contact_email')
    list_filter = ('date', 'time', 'session_type')

admin.site.register(Booking, BookingAdmin)
