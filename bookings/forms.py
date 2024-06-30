from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form for booking a session

    This form is used to create and update bookings. It includes
    custom validation for the date and contact number fields, and
    ensures no duplicate bookings for the same date and time.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the form

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        self.current_booking = kwargs.pop('current_booking', None)
        super().__init__(*args, **kwargs)

    class Meta:
        """
        Meta information for the BookingForm

        Attributes:
            model (Booking): The model to be used for the form
            fields (list): The fields to be included in the form
            widgets (dict): Custom widgets for the form fields
        """
        model = Booking
        fields = [
            'date', 'time', 'session_type', 'contact_number',
            'contact_email', 'additional_info'
        ]
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date', 'min': timezone.now().date().isoformat()
            }),
            'time': forms.Select(),
            'session_type': forms.Select(),
            'contact_number': forms.TextInput(attrs={'type': 'tel'}),
            'contact_email': forms.EmailInput(),
            'additional_info': forms.Textarea(attrs={
                'placeholder':
                'Any additional information please provide here...'
            }),
        }

    def clean_date(self):
        """
        Validate the date field

        Ensures the date is not in the past.

        Returns:
            datetime.date: The cleaned date

        Raises:
            forms.ValidationError: If the date is in the past
        """
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    def clean_contact_number(self):
        """
        Validate the contact number field

        Ensures the contact number contains only digits.

        Returns:
            str: The cleaned contact number

        Raises:
            forms.ValidationError:
            If the contact number contains non-digit characters
        """
        contact_number = self.cleaned_data['contact_number']
        if not contact_number.isdigit():
            raise forms.ValidationError(
                "Contact number must contain only digits.")
        return contact_number

    def clean(self):
        """
        Perform additional validation

        Ensures no duplicate bookings for the same date and time.

        Returns:
            dict: The cleaned data

        Raises:
            forms.ValidationError: If the time slot is already booked
        """
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            bookings = Booking.objects.filter(date=date, time=time)
            if self.current_booking:
                bookings = bookings.exclude(id=self.current_booking.id)
            if bookings.exists():
                raise forms.ValidationError(
                    "This time slot is already booked.")

        return cleaned_data
