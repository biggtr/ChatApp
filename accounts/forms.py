from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "profile_image",
        ]
        error_messages = {
            "username": {
                "unique": "Username already taken. Please choose a different one.",
            },
            "email": {
                "unique": "This Email is Already Taken. Please choose a different one.",
            },
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "profile_image",
        ]
