# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CusomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model   = CustomUser
        fields  = UserCreationForm.Meta.fields + ("user_type", "company")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model   = CustomUser
        fields  = UserChangeForm.Meta.fields