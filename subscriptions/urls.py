from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from subscriptions.views import CreateCheckoutSession

app_name = 'subscriptions'

urlpatterns = [
    path('unsubscribe/', views.newsletter_subscription_delete, name='newsletter-unsubscribe'),
    path('unsubscribed/', views.newsletter_subscription_confirmation, name='newsletter-unsubscribed'),
    
    path('subscription/products/', views.product, name='subscription-products'),
    # path('subscription/checkout/', views.subscription_checkout, name='subscription-checkout'),
    path('subscription/checkout/', CreateCheckoutSession.as_view(), name='subscription-checkout'), 
    path('subscription/success/', views.subscription_success, name='subscription-success'),
    path('subscription/cancel/', views.subscription_cancel, name='subscription-cancel'),
]