from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servidor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=75)
    setor = models.CharField(max_length=50)
    secretaria = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Tipo(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome do Serviço', blank=True)
    sigla = models.CharField(max_length=3, verbose_name="Sigla", blank=True)
    def __str__(self):
        return self.nome
    
class Chamado(models.Model):
    requisitante = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=150)
    dataAbertura = models.DateTimeField(auto_now_add=True)
    dataFechamento = models.DateTimeField(null=True, blank=False)
    