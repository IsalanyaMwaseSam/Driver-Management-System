# Generated by Django 3.2.12 on 2022-08-26 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver_app', '0007_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='driver',
        ),
    ]
