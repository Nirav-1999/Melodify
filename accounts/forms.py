from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username', 'email', )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=CustomUser
        fields=('username', 'email', )