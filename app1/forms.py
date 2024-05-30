from django import forms
from django.forms import ModelForm
#from django.contrib.auth.models import pan
from .models import *

class panecito(forms.ModelForm):
	class Meta:
		model=pan
		fields ='__all__'