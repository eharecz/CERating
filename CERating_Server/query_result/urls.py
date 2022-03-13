from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_result, name='query_result'),
    # path('recharge2/', views.recharge2, name="recharge2")
]