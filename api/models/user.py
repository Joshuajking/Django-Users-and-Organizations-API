import re
from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


# Create your models here
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password, phone=None, birthdate=None):
        """Creates new user profile"""
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, birthdate=birthdate)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True, default=None)
    birthdate = models.DateField(max_length=10, blank=True, null=True, default=None, help_text='Enter birthdate in YYYY-MM-DD format')
    organization = models.ForeignKey('OrganizationProfile', on_delete=models.CASCADE, blank=True, null=True, default=None)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def clean(self):
        if not self.is_superuser:
            if self.phone is not None and not self.validate_phone_number(self.phone):
                raise ValidationError('Invalid phone number')

            if self.birthdate is not None and self.birthdate > date.today():
                raise ValidationError('Birthday cannot be in the future')

    def save(self, *args, **kwargs):
        self.clean()
        super(UserProfile, self).save(*args, **kwargs)

    @staticmethod
    def validate_phone_number(phone_number):
        """Validates a phone number using a regular expression"""
        pattern = re.compile(r'^\+?[\d-]+$')
        return pattern.match(phone_number) is not None

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


