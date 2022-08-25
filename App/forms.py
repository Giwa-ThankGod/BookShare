from django import forms

class DonateForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget= forms.TextInput(
            attrs = {
                'class': 'form-control border-0 p-4',
                'placeholder': 'Name',
                'required': 'required',
            }
        )
    )

    email = forms.CharField(
        widget= forms.EmailInput(
            attrs = {
                'class': 'form-control border-0 p-4',
                'placeholder': 'Email',
                'required': 'required',
            }
        )
    )

    phone = forms.CharField(
        widget= forms.TextInput(
            attrs = {
                'class': 'form-control border-0 p-4',
                'placeholder': 'Phone Number',
                'required': 'required',
            }
        )
    )

    # category = forms.ChoiceField(
    #     choices= (('Computer','Computer',),('Business','Business'),),
    #     required = True,
    #     label= 'Select Book',
    #     widget= forms.Select(
    #         attrs = {
    #             'class': 'form-control border-0 p-4',
    #             'placeholder': 'Pick up address',
    #             'required': 'required',
    #             'cols': 30,
    #             'rows': 2,
    #         },
            
    #     )
    # )

    address = forms.CharField(
        widget= forms.Textarea(
            attrs = {
                'class': 'form-control border-0 p-4',
                'placeholder': 'Pick up address',
                'required': 'required',
                'cols': 30,
                'rows': 2,
            }
        )
    )

class NewsletterForm(forms.Form):
    email = forms.CharField(
        max_length=50,
        widget= forms.EmailInput(
            attrs = {
                'class': 'form-control border-light',
                'placeholder': 'Your Email Address',
                'style': "padding: 30px; border-top-left-radius: 5px; border-bottom-left-radius: 5px;",
            }
        )
    )