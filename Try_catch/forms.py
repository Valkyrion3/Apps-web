from django import forms
from .models import *

class NumerosForm(forms.ModelForm):
    class Meta:
        model = numeros
        fields = ['num1', 'num2','num3']