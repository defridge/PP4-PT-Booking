from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def get_current_date():
    return timezone.now().date()


SESSION_TYPE_CHOICES = [
    ('consultation', 'Consultation'),
    ('personal_training', 'Personal Training'),
]

TIME_CHOICES = [
    ('08:00', '8:00 AM - 9:00 AM'),
    ('09:00', '9:00 AM - 10:00 AM'),
    ('10:00', '10:00 AM - 11:00 AM'),
    ('11:00', '11:00 AM - 12:00 PM'),
    ('14:00', '2:00 PM - 3:00 PM'),
    ('15:00', '3:00 PM - 4:00 PM'),
    ('16:00', '4:00 PM - 5:00 PM'),
    ('17:00', '5:00 PM - 6:00 PM'),
]


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=get_current_date)
    time = models.CharField(max_length=20, choices=TIME_CHOICES)
    session_type = models.CharField(
        max_length=20, choices=SESSION_TYPE_CHOICES)
    duration = models.IntegerField(default=60)
    contact_number = models.CharField(max_length=15)
    contact_email = models.EmailField()
    additional_info = models.TextField(
        blank=False, null=False, max_length=1000)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return (f"{self.user.username} - {self.session_type} on "
                f"{self.date} at {self.time}")
