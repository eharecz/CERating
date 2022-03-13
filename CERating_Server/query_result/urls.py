from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_result, name='query_result')
]