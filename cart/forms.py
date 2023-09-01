from django.utils.translation import gettext_lazy as _
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,label=_('Quantity'))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)