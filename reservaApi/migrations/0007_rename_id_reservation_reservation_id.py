# Generated by Django 4.0.3 on 2022-03-16 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservaApi', '0006_rename_id_reservation_id_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='id_reservation',
            new_name='id',
        ),
    ]