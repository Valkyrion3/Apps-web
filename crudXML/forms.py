# forms.py
from django import forms
from .models import XMLFile

class XMLFileForm(forms.ModelForm):
    class Meta:
        model = XMLFile
        fields = ['name', 'file']

class XMLFileEditForm(forms.ModelForm):
    class Meta:
        model = XMLFile
        fields = ['name', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class XMLFileCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    color = forms.CharField(max_length=100)
    textura = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    modelo = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100)
    potencia = forms.IntegerField()
    vel_max = forms.IntegerField(label='Velocidad Máxima')
    tipo_transmision = forms.CharField(max_length=100, label='Tipo de Transmisión')
    tipo_combustible = forms.CharField(max_length=100, label='Tipo de Combustible')

class XMLFileValueEditForm(forms.Form):
    color = forms.CharField(max_length=100)
    textura = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    modelo = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100)
    potencia = forms.IntegerField()
    vel_max = forms.IntegerField(label='Velocidad Máxima')
    tipo_transmision = forms.CharField(max_length=100, label='Tipo de Transmisión')
    tipo_combustible = forms.CharField(max_length=100, label='Tipo de Combustible')