from rest_framework import serializers
from .models import Users, Organization


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "name", "phone", "email", "organization", "birthdate"]


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name", "phone", "address"]
