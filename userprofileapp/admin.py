from django.contrib import admin

# Register your models here.

from .models import UserProfile,profile

admin.site.register(UserProfile)
admin.site.register(profile)
