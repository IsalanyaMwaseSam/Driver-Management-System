from django.db import models
from django.conf import settings
from accounts.models import Account

# Create your models here.
class Info(models.Model):
    title = models.CharField(verbose_name="title", max_length=100, null=True)
    information = models.CharField(verbose_name="information", max_length=2000, null=True)

    def __str__(self):
        return self.title

class Cars(models.Model):
    type = models.CharField(verbose_name="type", max_length=100, null=True, blank=True)
    date = models.DateField(verbose_name='date', null=True, blank=True)
    number_Plate = models.CharField(verbose_name='Number Plate', max_length=100, null=True, unique=True, blank=True)
    cost = models.FloatField(verbose_name="cost", null=True, blank=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Cars'
        verbose_name_plural = 'Cars'

class Payment(models.Model):
    driver = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_made = models.FloatField(verbose_name='payment made', null=True, blank=False)
    balance = models.FloatField(verbose_name='balance', null=True, blank=False)
    date_of_payment = models.DateTimeField(verbose_name='date', null=True, blank=False)
    status = models.BooleanField(verbose_name='status', default=False, null=True, blank=False)

    def __str__(self):
        return self.driver


