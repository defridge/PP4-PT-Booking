from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Booking
from datetime import timedelta


class BookingTests(TestCase):
    """
    Test cases for the Booking model and views
    """

    def setUp(self):
        """
        Set up the test environment

        Creates a regular user and a staff member,
        and defines future dates for testing
        """
        self.user = User.objects.create_user(
            username='testuser', password='12345')

        self.staff_user = User.objects.create_user(
            username='staffuser', password='12345', is_staff=True)

        self.future_date1 = (timezone.now().date() + timedelta(days=1))
        self.future_date2 = (timezone.now().date() + timedelta(days=2))

    def test_create_booking_view(self):
        """
        Test the create booking view

        Ensures that a booking can be successfully created
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_booking'), {
            'date': self.future_date1.isoformat(),
            'time': '10:00',
            'session_type': 'personal_training',
            'duration': 60,
            'contact_number': '1234567890',
            'contact_email': 'test@example.com',
            'additional_info': 'No additional info'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.user, self.user)

    def test_manage_bookings_view(self):
        """
        Test the manage bookings view

        Ensures that bookings are listed correctly for the user
        """
        Booking.objects.create(
            user=self.user,
            date=self.future_date1,
            time='10:00',
            session_type='personal_training',
            duration=60,
            contact_number='1234567890',
            contact_email='test@example.com',
            additional_info='No additional info'
        )
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('manage_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/manage_bookings.html')
        formatted_date = self.future_date1.strftime('%B %-d, %Y')
        self.assertContains(response, formatted_date)

    def test_edit_booking_view(self):
        """
        Test the edit booking view

        Ensures that a booking can be successfully edited
        """
        booking = Booking.objects.create(
            user=self.user,
            date=self.future_date1,
            time='10:00',
            session_type='personal_training',
            duration=60,
            contact_number='1234567890',
            contact_email='test@example.com',
            additional_info='No additional info'
        )
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse(
            'edit_booking', args=[booking.id]), {
            'date': self.future_date2.isoformat(),
            'time': '11:00',
            'session_type': 'consultation',
            'duration': 60,
            'contact_number': '0987654321',
            'contact_email': 'update@example.com',
            'additional_info': 'Updated info'
        })
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(booking.date, self.future_date2)
        self.assertEqual(booking.time, '11:00')
        self.assertEqual(booking.session_type, 'consultation')
        self.assertEqual(booking.duration, 60)
        self.assertEqual(booking.contact_number, '0987654321')
        self.assertEqual(booking.contact_email, 'update@example.com')
        self.assertEqual(booking.additional_info, 'Updated info')

    def test_delete_booking_view(self):
        """
        Test the delete booking view

        Ensures that a booking can be successfully deleted
        """
        booking = Booking.objects.create(
            user=self.user,
            date=self.future_date1,
            time='10:00',
            session_type='personal_training',
            duration=60,
            contact_number='1234567890',
            contact_email='test@example.com',
            additional_info='No additional info'
        )
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse(
            'delete_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 0)

    def test_manage_client_bookings_view(self):
        """
        Test if a trainer can manage user bookings

        Ensures that a staff user can view and manage client bookings
        """
        Booking.objects.create(
            user=self.user,
            date=self.future_date1,
            time='10:00',
            session_type='personal_training',
            duration=60,
            contact_number='1234567890',
            contact_email='test@example.com',
            additional_info='No additional info'
        )
        self.client.login(username='staffuser', password='12345')
        response = self.client.get(reverse('manage_client_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
                response, 'bookings/manage_client_bookings.html')
        formatted_date = self.future_date1.strftime('%B %-d, %Y')
        self.assertContains(response, formatted_date)

    def test_edit_client_booking_view(self):
        """
        Test if a trainer can edit a client booking

        Ensures that a staff user can edit client bookings
        """
        booking = Booking.objects.create(
            user=self.user,
            date=self.future_date1,
            time='10:00',
            session_type='personal_training',
            duration=60,
            contact_number='1234567890',
            contact_email='test@example.com',
            additional_info='No additional info'
        )
        self.client.login(username='staffuser', password='12345')
        response = self.client.post(reverse(
            'edit_client_booking', args=[booking.id]), {
            'date': self.future_date2.isoformat(),
            'time': '11:00',
            'session_type': 'consultation',
            'duration': 60,
            'contact_number': '0987654321',
            'contact_email': 'update@example.com',
            'additional_info': 'Updated info'
        })
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(booking.date, self.future_date2)
        self.assertEqual(booking.time, '11:00')
        self.assertEqual(booking.session_type, 'consultation')
        self.assertEqual(booking.duration, 60)
        self.assertEqual(booking.contact_number, '0987654321')
        self.assertEqual(booking.contact_email, 'update@example.com')
        self.assertEqual(booking.additional_info, 'Updated info')

    def test_delete_client_booking_view(self):
        """
        Test if trainer can delete user booking

        Log in as a staff member and delete a client booking.
        Verify that the booking is removed.
        """
        booking = Booking.objects.create(
            user=self.user,
            date=self.future_date1,
            time='10:00',
            session_type='personal_training',
            duration=60,
            contact_number='1234567890',
            contact_email='test@example.com',
            additional_info='No additional info'
        )
        self.client.login(username='staffuser', password='12345')
        response = self.client.post(reverse(
            'delete_client_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 0)
