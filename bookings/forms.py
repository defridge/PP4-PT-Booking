from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'session_type', 'contact_number', 'contact_email', 'additional_info']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(),
            'session_type': forms.Select(),
            'contact_number': forms.TextInput(attrs={'type': 'tel'}),
            'contact_email': forms.EmailInput(),
            'additional_info': forms.Textarea(),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        
        if Booking.objects.filter(date=date, time=time).exists():
            raise forms.ValidationError("This time slot is already booked.")
        
        return cleaned_data
