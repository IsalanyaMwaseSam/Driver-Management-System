# Generated by Django 3.2.12 on 2022-08-29 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver_app', '0010_payment_balance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompletePayment',
        ),
    ]
