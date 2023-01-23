from django.db import models
import uuid

# Create your models here.
class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=50, unique=True)
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE)
    birthdate = models.DateField(help_text="Users Birthdate: 'MM/DD/YYYY'")

    def __str__(self):
        return self.name
