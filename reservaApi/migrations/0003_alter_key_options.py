# Generated by Django 4.0.3 on 2022-03-16 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservaApi', '0002_alter_key_numero'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='key',
            options={'ordering': ['numero'], 'verbose_name': 'Chave', 'verbose_name_plural': 'Chaves'},
        ),
    ]
