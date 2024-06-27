from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
from django.utils import timezone
from datetime import timedelta


class BookingTests(TestCase):

    def setUp(self):
        """
        Create a regular user
        """
        self.user = User.objects.create_user(
            username='testuser', password='12345')

        """
        Create a staff member (trainer)
        """
        self.staff_user = User.objects.create_user(
            username='staffuser', password='12345', is_staff=True)

        self.future_date1 = (timezone.now().date() + timedelta(days=1))
        self.future_date2 = (timezone.now().date() + timedelta(days=2))

    def test_create_booking_view(self):
        """
        Test create booking
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
        Test manage bookings
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
        formatted_date = self.future_date1.strftime('%B %d, %Y')  # Format the date to match the template output
        self.assertContains(response, formatted_date)

    def test_edit_booking_view(self):
        """
        Test edit booking
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
        Test delete booking
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
        Test if trainer can manage user bookings
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
        formatted_date = self.future_date1.strftime('%B %d, %Y')  # Format the date to match the template output
        self.assertContains(response, formatted_date)

    def test_edit_client_booking_view(self):
        """
        Test if trainer can edit client booking
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
