from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = ['nombre', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'color', 'precio', 'categoria']
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Selecciona una ccategoria"