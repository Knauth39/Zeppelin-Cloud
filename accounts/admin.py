# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CusomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CusomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "company",
        "user_type",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("company", "user_type")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("company", "user_type")}),)

admin.site.register(CustomUser, CustomUserAdmin)