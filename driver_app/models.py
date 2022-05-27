from django.db import models

# Create your models here.
class Info(models.Model):
    title = models.CharField(verbose_name="title", max_length=100, null=True)
    information = models.CharField(verbose_name="information", max_length=2000, null=True)

    def __str__(self):
        return self.title

class Cars(models.Model):
    type = models.CharField(verbose_name="type", max_length=100, null=True)
    date = models.DateField(verbose_name='date', null=True)
    number_plate = models.CharField(verbose_name='Number Plate', max_length=100, null=True, unique=True)
    cost = models.FloatField(verbose_name="cost", null=True)

    def __str__(self):
        return self.type