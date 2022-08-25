from django import forms
from Paystack.models import *

class PaymentForm(forms.ModelForm):
    class Meta:
         model = Payment
         fields = ['amount','first_name','last_name','email','shipping_address','phone']

         widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'shipping_address': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                    'cols': 2,
                    'rows': 2,
                }
            ),
            'phone': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
         }