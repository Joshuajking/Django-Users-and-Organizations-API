from django.contrib import admin
from api.models.models import UserProfile
from api.models.organization import OrganizationProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(OrganizationProfile)
