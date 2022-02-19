from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls.static import static
from .views import (
    newsletter_subscription_delete,
    newsletter_subscription_confirmation,
    product,
    product_create,
    product_update
)

app_name = 'subscriptions'

urlpatterns = [
    path('unsubscribe/', newsletter_subscription_delete, name='newsletter-unsubscribe'),
    path('unsubscribed/', newsletter_subscription_confirmation, name='newsletter-unsubscribed'),
    
    path('subscription/products/', product.as_view(), name='subscription-products'),
    path('subscription/products/create/', product_create, name='subscription-create'),
    path('subscription/products/update<pk>/', product_update, name='subscription-update'),
    #path('subscription/checkout/', views.subscription_checkout, name='subscription-checkout'),
    #path('subscription/checkout/', CreateCheckoutSession.as_view(), name='subscription-checkout'), 
    #path('subscription/success/', views.subscription_success, name='subscription-success'),
    #path('subscription/cancel/', views.subscription_cancel, name='subscription-cancel'),
]
