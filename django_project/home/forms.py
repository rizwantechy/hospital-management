from django import forms

from .models import Booking, Departments, Doctors, contact


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # to create form using booking model
        fields = '__all__'
        # labels = {  # to display form labels to specified name
        #     'p_name': 'Patient Name',
        #     'p_phone': 'Phone Number',
        #     'p_email': 'Email',
        #     'Doc_name': 'Doctor',
        #     'Booking_date': 'Booking Date',
        #
        #     # Add custom labels for other fields as needed
        # }

        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-light'}),
            'p_name': forms.TextInput(attrs={'class': 'form-control bg-light',}),
            'p_phone': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'p_email':forms.EmailInput(attrs={'class': 'form-control bg-light'}),
            'doc_name': forms.Select(attrs={'class': 'form-control bg-light'})

        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
        widgets = {
            'c_name': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'c_address': forms.TextInput(attrs={'class': 'form-control bg-light', }),
            'c_phone': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'c_email': forms.EmailInput(attrs={'class': 'form-control bg-light'}),
            'c_sub': forms.TextInput(attrs={'class': 'form-control bg-light'})

        }
