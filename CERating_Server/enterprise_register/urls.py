
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Enterprise_Register, name='enterprise_register'),
    
]
