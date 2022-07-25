from django import forms
from django.core.exceptions import ValidationError


class Userform(forms.Form):
    uid = forms.IntegerField()
    name = forms.CharField(max_length=30)
    age = forms.IntegerField(max_value=65, min_value=25)
    contact = forms.IntegerField()
    gender = forms.CharField()
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=10)

    def clean_contact(self):
        no = self.cleaned_data["contact"]  # it is used get data from input field
        if len(str(no)) == 10:
            return no
        else:
            raise ValidationError("invalid contact Number")
