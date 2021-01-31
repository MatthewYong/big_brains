from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email_address', 'address',
                  'postcode', 'town', 'country', 'comments')

    def __init__(self, *args, **kwargs):
        """
        Function to add placeholders and classes,
        code used from CI checkout lesson
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'address': 'Address',
            'postcode': 'Postcode',
            'town': 'Town',
            'country': 'Country',
            'comments': 'Add your comments',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
