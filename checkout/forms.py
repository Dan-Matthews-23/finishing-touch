from django import forms
from .models import UserProfile



class BasketForm(forms.ModelForm):
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