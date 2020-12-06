from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import StudentRegistration


class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=14)

    class Meta:
        model = User
        fields = ("first_name", "last_name",
                  "username", "password1", "password2")
