from rest_framework import serializers
from api.models.user import UserProfile
from api.models.organization import OrganizationProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["id", "name", "phone", "email", "organization", "birthdate", "password"]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProfile
        fields = ["id", "name", "phone", "address"]
