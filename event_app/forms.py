from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name must start with z')

class EditForm(forms.Form):

    event_name = forms.CharField(
        label='Name',
        max_length=264,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[check_for_z]
    )

    event_logo = forms.FileField()

    event_from_date = forms.CharField(
        label='From Date',
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'fromDate'
            }
        )
    )

    event_to_date = forms.CharField(
        label='To Date',
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'toDate'
            }
        )
    )

    botcacher = forms.CharField(required=False, widget=forms.TextInput, validators=[validators.MaxLengthValidator(0,message='Gotcha Bot')])
