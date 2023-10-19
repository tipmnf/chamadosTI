from django import forms
from django.forms import ModelForm, ValidationError, Form
from .models import *
from django.contrib.auth.models import Group
from django.forms import ModelChoiceField
from django.core.validators import MinValueValidator, MaxValueValidator

class Chamado_Form(ModelForm):
    class Meta:
        model = Chamado
        widgets = {
            'tipo': forms.Select(attrs={'readonly': True}),
        }
        exclude = ['dataAbertura', 'dataFechamento', 'prioridade', 'status', 'numero', 'atendente']
        
class SearchForm(Form):
    
    # ANO_CHOICES = [(None,'-')]+[(year, year) for year in range(2000, 2101)]
    # MES_CHOICES = [(None,'-')]+[(month, month) for month in range(1, 13)]
    # DIA_CHOICES = [(None,'-')]+[(day, day) for day in range(1, 32)]
    REQUISITANTE_CHOICES = [(False,'-')]+[(obj.id, obj.nome) for obj in Servidor.objects.all()]
    TIPO_CHOICES = [(False,'-')]+[(obj.id, obj.sigla) for obj in Tipo.objects.all()]
    SECRETARIA_CHOICES = [(False,'-')]+[(obj.id, obj.nome) for obj in Secretaria.objects.all()]
    SETOR_CHOICES = [(False,'-')]+[(obj.id, obj.nome) for obj in Setor.objects.all()]
    
    numero = forms.CharField(label='Numero', max_length=10, required=False)
    assunto = forms.CharField(label='Assunto', required=False)
    requisitante = forms.ChoiceField(label='Requisitante', choices=REQUISITANTE_CHOICES, required=False)
    tipo = forms.ChoiceField(label='Tipo', choices=TIPO_CHOICES, required=False)
    secretaria = forms.ChoiceField(label='Secretaria', choices=SECRETARIA_CHOICES, required=False)
    setor = forms.ChoiceField(label='Setor', choices=SETOR_CHOICES, required=False)
    # ano = forms.ChoiceField(choices=ANO_CHOICES, required=False)
    # mes = forms.ChoiceField(choices=MES_CHOICES, required=False)
    # dia = forms.ChoiceField(choices=DIA_CHOICES, required=False)
    
    