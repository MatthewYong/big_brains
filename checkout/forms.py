from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email_address', 'address',
                  'postcode', 'town', 'country', 'comments')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'First Name'}),
            'comments': forms.Textarea(attrs={
                'class': 'textarea', 'rows': 5,
                'placeholder': 'Comments'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Function to add placeholders and classes,
        code used from CI checkout lesson
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = False
