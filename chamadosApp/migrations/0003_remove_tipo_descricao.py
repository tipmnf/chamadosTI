# Generated by Django 4.2.5 on 2023-10-10 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamadosApp', '0002_alter_tipo_nome_alter_tipo_sigla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo',
            name='descricao',
        ),
    ]