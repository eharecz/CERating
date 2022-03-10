from django.urls import path
from . import views

urlpatterns = [
    path('', views.enterprise_simurate, name='SimuRate_times_query'),

]