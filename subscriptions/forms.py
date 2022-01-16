from django import forms
from . models import newsletterSubscribers


class SubsciberForm(forms.ModelForm):
    class Meta:
        model = newsletterSubscribers
        fields = ['email']