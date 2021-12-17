from django import forms
from django.forms import fields
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'