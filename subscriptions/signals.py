# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from .models import CustomerSubscriptions


# def confirm_subscription(sender, instance, created, **kwargs):
#     if created:
#         # Adds Username to the Profile Model
#         CustomerSubscriptions.objects.create(
# 			user=instance,
# 			name=instance.username,
#             stripe_subscription_id = instance.stripe_subscription_id,
# 			)

# post_save.connect(confirm_subscription, sender=User)