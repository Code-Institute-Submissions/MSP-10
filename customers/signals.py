from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        # Adds Username to the Profile Model
        Profile.objects.create(
			user=instance,
			name=instance.username,
			)

post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        print('Profile updated!')
        
post_save.connect(update_profile, sender=User)