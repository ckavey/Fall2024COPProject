"""
URL configuration for library_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from fines_donations.views import success_view, profile_view, settings_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fines_donations.urls')),
    path('accounts/', include('allauth.urls')),  # Include allauth routes
    path('', TemplateView.as_view(template_name='fines_donations/index.html'), name='home'),
    path('success/', success_view, name='success'),
    path('profile/', profile_view, name='profile'),
    path('settings/', settings_view, name='settings'),
]
