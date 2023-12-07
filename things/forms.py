"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MaxLengthValidator

class ThingForm(forms.ModelForm):
    name = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea, max_length=120)
    quantity = forms.NumberInput()
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
