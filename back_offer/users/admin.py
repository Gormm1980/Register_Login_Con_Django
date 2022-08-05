from users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

# Register your models here.
