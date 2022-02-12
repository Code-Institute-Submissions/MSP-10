from django import forms
from . models import newsletterSubscribers, Subscription
from crispy_forms.helper import FormHelper


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = newsletterSubscribers
        fields = ['email']
        

class SubscriptionCreate(forms.ModelForm):
    # Form to Create a new subscription product
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Subscription Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Provider description'}))
    stripe_subscription_id = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Stripe ID'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': '€00.00'}))

    def __init__(self, *args, **kwargs):
        super(SubscriptionCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Subscription
        fields = ['name', 'description', 'stripe_subscription_id', 'price']
