# Generated by Django 4.0.3 on 2022-04-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_perfil_cep_alter_perfil_cpf_alter_perfil_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cep',
            field=models.CharField(max_length=8),
        ),
    ]
