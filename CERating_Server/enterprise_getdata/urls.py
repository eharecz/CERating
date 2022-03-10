from django.urls import path
from . import views

urlpatterns = [
    path('', views.getEnterpriseData, name='enterprise_getData'),
]
