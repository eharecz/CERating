from django.urls import path
from . import views

urlpatterns = [
    path('', views.recharge, name='recharge'),

]