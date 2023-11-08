from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    Field_form = forms.CharField(max_length=30)


class EmailForm(forms.Form):
    text = forms.CharField
    boolean = forms.BooleanField
    integer = forms.IntegerField
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.is_valid():
            raise forms.ValidationError("Invalid an email")
        return email


class TestForm(forms.Form):
    text = forms.CharField(min_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()

    def clean_integer(self):
        integer = self.cleaned_data.get("integer")
        if integer <= 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer