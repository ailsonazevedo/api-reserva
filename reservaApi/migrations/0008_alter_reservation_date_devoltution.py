# Generated by Django 4.0.3 on 2022-03-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaApi', '0007_rename_id_reservation_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_devoltution',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data da Devolução'),
        ),
    ]