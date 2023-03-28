from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.conf import settings


class OrganizationProfileManager(BaseUserManager):
    """Manager for Organization profiles"""
    def create_organization(self, name, phone, address):
        """Create a new organization profile"""

        organization = self.model(name=name)

        organization.save(using=self._db)

        return organization


class OrganizationProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for Organizations in the system"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
