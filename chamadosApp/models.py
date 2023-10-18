from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Secretaria(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    secretaria = models.ForeignKey(Secretaria, verbose_name="Secretaria", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default='')
    cep = models.CharField(max_length=8, default='')
    bairro = models.CharField(max_length=50, default='')
    logradouro = models.CharField(max_length=150, default='')
    
    def __str__(self):
        return self.nome
    
class Servidor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=75)
    secretaria = models.ForeignKey(Secretaria, verbose_name='Secretaria', on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, verbose_name='Setor', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Tipo(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome do Serviço', blank=True)
    sigla = models.CharField(max_length=3, verbose_name="Sigla", blank=True)
    descricao = models.TextField(default='')
    
    def __str__(self):
        return self.nome
    
class Chamado(models.Model):
    
    prioridadeChoices = (
        ('0', 'Baixa'),
        ('1', 'Média'),
        ('2', 'Alta')
    )
    
    statusChoices = (
        ('0', 'Aberto'),
        ('1', 'Pendente'),
        ('2', 'Resolvido'),
        ('3', 'Finalizado')
    )
    
    secretaria = models.ForeignKey(Secretaria, verbose_name='Secretaria', on_delete=models.CASCADE, null=True)
    setor = models.ForeignKey(Setor, verbose_name='Setor', on_delete=models.CASCADE, null=True)
    requisitante = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=150)
    prioridade = models.CharField(max_length=1, choices=prioridadeChoices, default='0')
    status = models.CharField(max_length=1, choices=statusChoices, default='0')
    descricao = models.TextField(default='')
    dataAbertura = models.DateTimeField(auto_now_add=True)
    dataFechamento = models.DateTimeField(null=True, blank=False)
    
class Atendente(Servidor):
    tipo = models.ManyToManyField(Tipo, verbose_name='Tipo')