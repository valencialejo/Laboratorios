# Generated by Django 3.1.3 on 2021-08-16 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Plataforma', '0010_auto_20210816_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
    ]