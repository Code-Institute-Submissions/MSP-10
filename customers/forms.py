from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Feedback, Contact


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'address1',
            'address2',
            'address3',
            'city',
            'postcode',
            'country'
        ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'comments']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subscription', 'email', 'comments']
