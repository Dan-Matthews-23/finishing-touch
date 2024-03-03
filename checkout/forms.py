from django import forms
from .models import Orders












class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('customer_name', 'customer_email', 'customer_tel_number',
                  'customer_address_one', 'customer_address_two',
                  'customer_address_three', 'customer_address_four', 'customer_postcode',)

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_name': 'Full Name',
            'customer_email': 'Email Address',
            'customer_tel_number': 'Phone Number',            
            'customer_postcode': 'Postal Code',
            'customer_address_three': 'Town or City',
            'customer_address_one': 'Street Address 1',
            'customer_address_two': 'Street Address 2',
            'customer_address_four': 'County',
        }

        self.fields['customer_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False