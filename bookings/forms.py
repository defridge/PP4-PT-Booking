from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['day', 'time', 'session_type', 'contact_number', 'contact_email', 'additional_info']
        widgets = {
            'day': forms.Select(),
            'time': forms.Select(),
            'session_type': forms.Select(),
            'contact_number': forms.TextInput(attrs={'type': 'tel'}),
            'contact_email': forms.EmailInput(),
            'additional_info': forms.Textarea(),
        }

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('day')
        time = cleaned_data.get('time')
        
        if Booking.objects.filter(day=day, time=time).exists():
            raise forms.ValidationError("This time slot is already booked.")
        
        return cleaned_data

    def clean_contact_email(self):
        email = self.cleaned_data.get('contact_email')
        if not email:
            raise forms.ValidationError("This field is required.")
        # Additional custom validation can be added here
        return email
