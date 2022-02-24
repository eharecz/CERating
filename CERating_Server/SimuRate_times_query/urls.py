from django.urls import path
from . import views

urlpatterns = [
    path('', views.SimuRate_times_query, name='SimuRate_times_query'),

]