from django.urls import path
from . import views

urlpatterns = [
    path('', views.recharge, name='recharge'),
    path('recharge2/', views.recharge2, name="recharge2")
]