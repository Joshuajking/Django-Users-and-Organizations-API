from rest_framework import serializers
from api.models.models import UserProfile
from api.models.organization import OrganizationProfile


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "name", "phone", "email", "organization", "birthdate"]


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProfile
        fields = ["id", "name", "phone", "address"]
