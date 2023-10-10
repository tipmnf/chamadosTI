from django import forms
from django.forms import ModelForm, ValidationError
from .models import Chamado
from django.contrib.auth.models import Group
from django.forms import ModelChoiceField

class Chamado_Form(ModelForm):
    class Meta:
        model = Chamado
        widgets = {
            'tipo': forms.Select(attrs={'readonly': True}),
        }
        exclude = ['dataAbertura', 'dataFechamento']