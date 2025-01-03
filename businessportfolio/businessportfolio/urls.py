"""
URL configuration for businessportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog-details/', views.blog_details, name='blog_details'),  
    path('blog/', views.blog, name='blog'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),  
    path('service-details/', views.service_details, name='service_details'),  
    path('starter-page/', views.starter_page, name='starter_page'),  
]
