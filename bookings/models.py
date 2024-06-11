from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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

DAY_CHOICES = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default='monday')
    time = models.CharField(max_length=5, choices=TIME_CHOICES, default='08:00')
    session_type = models.CharField(max_length=20, choices=SESSION_TYPE_CHOICES, default='consultation')
    duration = models.IntegerField(default=60)
    contact_number = models.CharField(max_length=15, default='000-000-0000')
    contact_email = models.EmailField(default='default@example.com')
    additional_info = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.session_type} on {self.day} at {self.time}"


