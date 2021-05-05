from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import User, Profile


# admin.site.register(CustomUserAdmin)
admin.site.register(User)
admin.site.register(Profile)