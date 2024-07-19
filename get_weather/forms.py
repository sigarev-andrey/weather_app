from django import forms
from .models import *

class MainForm(forms.Form):
    city = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'id': 'city',
            'placeholder': 'Город',
            'required': 'required'
        })