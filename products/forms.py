from django import forms
from products.models import Products



class ProductManagementForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            'product_id',
            'product_placeholder_name',
            'product_short_description', 
            'product_name', 
            'product_price',            
            'protein_source',
            'fibre_source', 
            'product_image_url', 
            'category_id',
            'calorie_content',
            'protein_content',
            'fibre_content',
            'fat_content',
            'saturated_fat_content',
            'carbohydrate_content',
            'carbohydrate_sugar_content',
            'salt_content',
            )

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        placeholders = {
            'product_placeholder_name': 'None display name of product',
            'product_short_description': 'Short description',
            'product_name': 'Display name of product',           
            'product_price': 'Product price',
            'protein_source': 'Yes/No',
            'fibre_source': 'Yes/No',
            'product_image_url': 'URL of product image',
            'category_id': '9',
            'calorie_content': 'Calorie content',
            'protein_content': 'Protein content',
            'fibre_content': 'Fibre content',
            'fat_content': 'Fat content',                        
            'saturated_fat_content': 'Saturated fat content',            
            'carbohydrate_content': 'Carbohydrate content',
            'carbohydrate_sugar_content': 'Sugar content',
            'salt_content': 'Salt content',
        }

        #self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'county':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            #self.fields[field].label = True