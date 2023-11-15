from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_phone_number(phonenumber):
    if re.search(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',phonenumber) == None:
        raise ValidationError(
            _("неверный формат номера телефона")
        )


class PostForm(forms.Form):
    Email = forms.EmailField()
    Telephone = forms.CharField(max_length=20, validators=[validate_phone_number])
    Date = forms.DateField()
    Text = forms.CharField()