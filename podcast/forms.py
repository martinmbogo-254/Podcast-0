from django import forms
from .models import Rating

class RateForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['rate','comment']
