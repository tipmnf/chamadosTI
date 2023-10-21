# Generated by Django 4.1.7 on 2023-10-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamadosApp', '0011_alter_chamado_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('0', 'Aberto'), ('1', 'Pendente'), ('2', 'Finalizado')], default='0', max_length=1),
        ),
    ]