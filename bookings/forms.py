from django import forms
from .models import Booking
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'date', 'time', 'session_type', 'contact_number',
            'contact_email', 'additional_info']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date', 'min': timezone.now().date().isoformat()}),
            'time': forms.Select(),
            'session_type': forms.Select(),
            'contact_number': forms.TextInput(attrs={'type': 'tel'}),
            'contact_email': forms.EmailInput(),
            'additional_info': forms.Textarea(attrs={
                'placeholder':
                'Any additional information please provide here...'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    def clean_contact_number(self):
        contact_number = self.cleaned_data['contact_number']
        if not contact_number.isdigit():
            raise forms.ValidationError(
                "Contact number must contain only digits.")
        return contact_number

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if Booking.objects.filter(date=date, time=time).exists():
            raise forms.ValidationError("This time slot is already booked.")

        return cleaned_data
