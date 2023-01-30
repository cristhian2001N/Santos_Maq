from datetime import datetime

from django import forms
from django.forms import ModelForm

from maquinari.models import Maquinaria


class MaquinariaForm(ModelForm):
    class Meta:
        model = Maquinaria
        fields = '__all__'
        exclude=['usuario']

        widgets = {
            'Descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese Descripcion'}),
            'Cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la Cantidad'}),

        }

