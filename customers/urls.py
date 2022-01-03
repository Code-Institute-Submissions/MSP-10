from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'customers'

urlpatterns = [
    path('customers/login/', views.loginPage, name='login-page'),
    path('customers/register/', views.register, name='register'),
]