# Generated by Django 4.1.7 on 2023-10-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamadosApp', '0008_chamado_atendente_alter_chamado_requisitante'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='numero',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
