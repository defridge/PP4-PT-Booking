from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('manage/', views.manage_bookings, name='manage_bookings'),
    path('manage_clients/', views.manage_client_bookings, name='manage_client_bookings'),
    path('success/', views.booking_success, name='booking_success'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('edit_client/<int:booking_id>/', views.edit_client_booking, name='edit_client_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('delete_client/<int:booking_id>/', views.delete_client_booking, name='delete_client_booking'),
]
