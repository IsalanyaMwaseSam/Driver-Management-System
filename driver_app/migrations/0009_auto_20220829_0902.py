# Generated by Django 3.2.12 on 2022-08-29 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver_app', '0008_rename_user_payment_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_made',
            field=models.FloatField(null=True, verbose_name='payment made'),
        ),
        migrations.CreateModel(
            name='CompletePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_made', models.FloatField(null=True, verbose_name='payment made')),
                ('balance', models.FloatField(null=True, verbose_name='balance')),
                ('date_of_payment', models.DateTimeField(null=True, verbose_name='date')),
                ('status', models.BooleanField(default=False, null=True, verbose_name='status')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
