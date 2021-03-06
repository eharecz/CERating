"""CERating_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='index'),
    path('email_request/', views.email_verification_code),
    path('getEnterpriseData/', include("enterprise_getdata.urls")),
    path('enterprise_register/',include("enterprise_register.urls")),
    path('enterprise_simurate/',include("enterprise_simurate.urls")),
    path('enterprise_recharge/',include("enterprise_recharge.urls")),
    path('query_result/',include("query_result.urls")),
    path('', include('web.urls'))
]
