# Generated by Django 3.1.3 on 2021-08-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plataforma', '0008_auto_20210816_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio_t', models.FloatField()),
                ('user', models.CharField(max_length=15, verbose_name='usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='user',
        ),
    ]