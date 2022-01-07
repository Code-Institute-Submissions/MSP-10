from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # leaving for now, need to work out how to remove the case sensitivity of register and login
    # def clean_username(self):
    #     # transform username to lowercase to remove default case sensitivity
    #     username = self.cleaned_data['username'].lower()
    #     filterusername = User.objects.filter(username=username)
    #     if filterusername.count():
    #         raise ValidationError("Username already exists")
    #     return username

    # def clean_email(self):
    #     # transform email to lowercase to remove default case sensitivity
    #     email = self.cleaned_data['email'].lower()
    #     filteremail = User.objects.filter(email=email)
    #     if filteremail.count():
    #         raise ValidationError("Email already exists")
    #     return email

    # def save(self):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email']
    #     )
    #     return user

