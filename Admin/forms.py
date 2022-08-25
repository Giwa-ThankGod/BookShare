from tkinter import Widget
from django import forms
from App.models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            )
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['ref'] #exclude ref, so that the form can be validated when submitted
    
        widgets= { 
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                    'cols': 30,
                    'rows': 5,
                }
            ),
            'price': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                    'min': 0
                }
            ),
            'cover': forms.ClearableFileInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'category': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                },
            ),
            'author': forms.Select(
                attrs = {
                    'class': 'form-control',
                },        
            ),

        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            #Used ClearableFileInput instead of FileInput to previous value
            'thumb': forms.ClearableFileInput(
                attrs = {
                    'class': 'form-control',
                }
            )

        }