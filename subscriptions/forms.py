from django import forms
from . models import newsletterSubscribers


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = newsletterSubscribers
        fields = ['email']