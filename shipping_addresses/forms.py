from django.forms import ModelForm
from .models import ShippingAddress

class ShippingAddressForm(ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = [
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'postal_code',
            'reference'
        ]
        labels = {
            'line1': 'Calle 1',
            'line2': 'Calle 2',
            'city': 'Ciudad',
            'state': 'Estado',
            'country': 'País',
            'postal_code': 'Código Postal',
            'reference': 'Referencias'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = [
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'postal_code',
            'reference'
        ]
        for field in fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
