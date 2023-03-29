from django.db import models


class OrganizationProfileManager(models.Manager):
    """Manager for Organization profiles"""
    def create_organization(self, name):
        """Create a new organization profile"""

        organization = self.model(name=name)

        organization.save(using=self._db)

        return organization


class OrganizationProfile(models.Model):
    """Database model for Organizations in the system"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
