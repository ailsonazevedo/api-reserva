# Generated by Django 3.2.12 on 2022-03-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaApi', '0011_rename_date_devoltution_reservation_date_devolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='numero',
            field=models.IntegerField(verbose_name='Número da chave'),
        ),
    ]