# Generated by Django 4.0.5 on 2022-07-04 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamilia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familia',
            old_name='licenciaConducirActivata',
            new_name='licenciaConducirActivada',
        ),
    ]
