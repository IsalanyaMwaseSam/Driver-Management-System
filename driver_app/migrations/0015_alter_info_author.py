# Generated by Django 3.2.12 on 2022-09-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_app', '0014_auto_20220913_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]
