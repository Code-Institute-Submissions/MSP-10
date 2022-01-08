from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'customers'

urlpatterns = [
    path('customers/login/', views.loginPage, name='login-page'),
    path('customers/register/', views.registerPage, name='register-page'),
    path('customers/logout/', views.logoutPage, name='logout-page'),
    
    path('customers/reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('customers/reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('customers/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('customers/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]