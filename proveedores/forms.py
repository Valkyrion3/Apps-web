from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
    estado = forms.BooleanField(required=False, widget=forms.Select(choices=((True, 'Activo'), (False, 'Inactivo'))))
    class Meta:
        model = categoria
        fields = ['nombre', 'estado']

class PiezaForm(forms.ModelForm):
    estado = forms.BooleanField(required=False, widget=forms.Select(choices=((True, 'Activo'), (False, 'Inactivo'))))
    class Meta:
        model = pieza
        fields = ['nombre', 'color', 'precio', 'categoria', 'stock', 'estado']
    def __init__(self, *args, **kwargs):
        super(PiezaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Selecciona una ccategoria"
    
class ProveedorForm(forms.ModelForm):
    estado = forms.BooleanField(required=False, widget=forms.Select(choices=((True, 'Activo'), (False, 'Inactivo'))))
    class Meta:
        model = proveedor
        fields = ['nombre', 'direccion', 'numero', 'ciudad', 'provinicia', 'estado']

class SuministroForm(forms.ModelForm):
    estado = forms.BooleanField(required=False, widget=forms.Select(choices=((True, 'Activo'), (False, 'Inactivo'))))
    class Meta:
        model = suministro
        fields = ['proveedor', 'fecha', 'monto', 'estado']

    def __init__(self, *args, **kwargs):
        super(SuministroForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].empty_label = "Selecciona un proveedor"
        self.fields['fecha'].widget = forms.widgets.DateInput(attrs={'type': 'date'})

class DetallesForm(forms.ModelForm):
    class Meta:
        model = suministro_pieza
        fields = ['suministro', 'pieza', 'cantidad', 'precio']

    def __init__(self, *args, **kwargs):
        super(DetallesForm, self).__init__(*args, **kwargs)
        self.fields['suministro'].empty_label = "Selecciona un suministro"
        self.fields['pieza'].empty_label = "Selecciona una pieza"