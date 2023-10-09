from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servidor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=75)
    setor = models.CharField(max_length=50)
    secretaria = models.CharField(max_length=50)
    
class Tipo(models.Model):
    nome = models.CharField(max_length=20)
    sigla = models.CharField(max_length=3)
    descricao = models.CharField(max_length=1000)
    
class Chamado(models.Model):
    requisitante = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=150)
    dataAbertura = models.DateTimeField(auto_now_add=True)
    dataFechamento = models.DateTimeField(null=True, blank=False)
    