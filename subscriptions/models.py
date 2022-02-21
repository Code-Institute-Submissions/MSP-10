from django.db import models
from django.contrib.auth.models import User


# Model for the newsletter subscription
class newsletterSubscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Model for the Available subscription packages
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    stripe_subscription_id = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    coffee = models.IntegerField(default=0)
    accessory = models.IntegerField(default=0)
    treats = models.IntegerField(default=0)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return str(self.name)

    def __str__(self):
        return str(self.stripe_subscription_id)


# Model that links the customers subscription with their account
class CustomerSubscriptions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def __str__(self):
        return str(self.stripe_subscription_id)
