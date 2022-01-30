from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('unsubscribe/', views.newsletter_subscription_delete, name='newsletter-unsubscribe'),
    path('unsubscribed/', views.newsletter_subscription_confirmation, name='newsletter-unsubscribed'),
    
    path('products/', views.product, name='subscription-products'),
    path('checkout/', views.subscription_checkout, name='subscription-checkout'),
    path('success/', views.subscription_success, name='subscription-success'),
    path('cancel/', views.subscription_cancel, name='subscription-cancel'),
]
