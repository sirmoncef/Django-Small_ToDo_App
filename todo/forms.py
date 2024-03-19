from django import forms
from .models import db

class Forem(forms.ModelForm):
    
    class Meta:
        model = db
        fields = '__all__'
