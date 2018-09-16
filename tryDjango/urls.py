"""tryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contact_view, about_view, api

from products.views import product_detail_view, product_create_view, product_list_view

urlpatterns = [
    
    path('product/', include('products.urls')),
    path('api/', api, name="Api"),
    path('contact/', contact_view, name="Contact"),
    path('about/', about_view, name="About"),
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
]
