# Generated by Django 4.2.5 on 2023-10-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamadosApp', '0006_remove_setor_endereco_setor_bairro_setor_cep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.RemoveField(
            model_name='atendente',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nome',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nome do Serviço'),
        ),
        migrations.AddField(
            model_name='atendente',
            name='tipo',
            field=models.ManyToManyField(to='chamadosApp.tipo', verbose_name='Tipo'),
        ),
    ]
