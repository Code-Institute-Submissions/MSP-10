from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

app_name = 'subscriptions'

urlpatterns = [
    # path('subs/', views.login_page, name='login-page'),
]
