# Generated by Django 4.0.3 on 2022-03-16 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservaApi', '0005_alter_reservation_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='id',
            new_name='id_reservation',
        ),
    ]
