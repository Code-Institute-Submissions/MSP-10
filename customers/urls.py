from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

app_name = 'customers'

urlpatterns = [
    path('customers/login/', views.login_page, name='login-page'),
    path('customers/register/', views.register_page, name='register-page'),
    path('customers/logout/', views.logout_page, name='logout-page'),
    
    path('customers/profile/<str:pk>/',views.customer_profile_view, name='customer-profile'),
    path('customers/profile/<str:pk>/update',views.customer_profile_update, name='customer-update'),
    path('customers/profile/<str:pk>/delete',views.customer_profile_delete, name='customer-delete'),
    
    path('customers/reset_password/', 
        auth_views.PasswordResetView.as_view(
            template_name='password/password_reset_form.html',
            success_url=reverse_lazy('customers:password_reset_done'),
            email_template_name='password/password_reset_email.html'), 
            name="reset_password"
    ),
    path('customers/reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='password/password_reset_done.html'
        ),
        name="password_reset_done"),
    path(
        'password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password/password_reset_confirm.html',
            success_url=reverse_lazy('customers:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    path('customers/reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password/password_reset_complete.html'),
        name="password_reset_complete"
    ),
]
