from django import forms
from .models import TripBooking
from .models import Contact

class TripBookingForm(forms.ModelForm):
    class Meta:
        model = TripBooking
        fields = '__all__'  # or specify fields if needed


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

