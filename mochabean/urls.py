from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('policies/', views.policies, name='policies'),
    path('shipping/', views.shipping, name='shipping'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('', include('customers.urls', namespace='customers')),
    path('', include('subscriptions.urls', namespace='subscriptions')),
    ]

# Custom Error pages
handler404 = views.error_404
