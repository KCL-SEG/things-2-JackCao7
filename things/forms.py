"""Forms of the project."""
from django import forms


class ThingForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.Textarea()
    quantity = forms.NumberInput()
    