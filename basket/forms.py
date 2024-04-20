"""from django import forms
from accounts.models import UserProfile
from .models import Orders



class OrderForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Basket Full Name',
            'email': 'Basket Email Address',
            'phone_number': 'Basket Phone Number',
            'postcode': 'Basket Postal Code',
            'town_or_city': 'Basket Town or City',
            'street_address1': 'Basket Street Address 1',
            'street_address2': 'Basket Street Address 2',
            'county': 'Basket County / district',
            
        }

        #self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_postcode':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False
            """

















from django import forms
from checkout.models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'county':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False