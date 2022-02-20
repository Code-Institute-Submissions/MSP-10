from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path, include
from django.conf.urls.static import static
from .views import (
    newsletter_subscription_delete,
    newsletter_subscription_confirmation,
    product,
    product_create,
    product_update,
    product_delete,
    subscription_checkout,
    subscription_success,
    subscription_unsuccess,
    customer_subscription
)

app_name = 'subscriptions'

urlpatterns = [
    # Newsletter subscription urls
    path(
        'unsubscribe/', 
        newsletter_subscription_delete, 
        name='newsletter-unsubscribe'),
    path(
        'unsubscribed/', 
        newsletter_subscription_confirmation, 
        name='newsletter-unsubscribed'),
    
    # Subscription Product urls
    path(
        'subscription/products/', 
        product.as_view(), 
        name='subscription-products'),
    path(
        'subscription/products/create/', 
        product_create, 
        name='subscription-create'),
    path(
        'subscription/products/update<pk>/', 
        product_update, 
        name='subscription-update'),
    path(
        'subscription/products/delete<pk>/', 
        product_delete, 
        name='subscription-delete'),
    path(
        'subscription/checkout<pk>/', 
        subscription_checkout, 
        name='subscription-checkout'),
    path('subscription/unsuccess/', subscription_unsuccess, name='subscription-unsuccess'),
    path('subscription/success/<pk>', subscription_success, name='subscription-success'),
    path('subscription/customer/', customer_subscription, name='subscription-customer'),
]
