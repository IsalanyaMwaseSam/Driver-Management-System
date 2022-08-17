from distutils.command.upload import upload
import email
from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

class MyAccountManager(BaseUserManager):
    def _create_user(self, email, username, address, phone_number, car, details, password):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
               email = self.normalize_email(email),
               username = username, address = address,
               phone_number = phone_number, car=car, details=details, password=password
            )   

        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_user(self, email, username, address=None, phone_number=None, car=None, details=None, password=None):
        return self._create_user(email, username, address, phone_number, car, details, password)

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email=email,
            username=username,
            password=password,
            
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(verbose_name='username', unique=True, max_length=60, null=True)
    address = models.CharField(verbose_name='address', max_length=200, null=True)
    phone_number = models.IntegerField(verbose_name='phone_number', null=True)
    car = models.CharField(verbose_name='car' , max_length=60, blank=False, null=True)
    details = models.CharField(verbose_name='details',  unique=True, max_length=60, blank=False, null=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = MyAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'static/images')