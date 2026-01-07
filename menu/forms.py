
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'guest_number',
            'date',
            'creneau',
            'comment'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guest_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'creneau': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        creneau = cleaned_data.get('creneau')

        if Booking.objects.filter(date=date, creneau=creneau).exists():
            raise forms.ValidationError(
                "Ce créneau est déjà réservé pour cette date."
            )
        return cleaned_data
