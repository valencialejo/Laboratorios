# Generated by Django 3.1.3 on 2021-08-16 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Plataforma', '0012_auto_20210816_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='laboratorio',
        ),
        migrations.DeleteModel(
            name='Laboratorio',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
