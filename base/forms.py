from django import forms
from .models import TravelPost

class TravelPostForm(forms.ModelForm):
    class Meta:
        model = TravelPost
        fields = ['name', 'text', 'tags']