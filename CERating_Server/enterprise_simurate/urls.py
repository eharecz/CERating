from django.urls import path
from . import views

urlpatterns = [
    path('', views.enterprise_simurate, name='SimuRate_times_query'),
    path('getEnterpriseRating/', views.getEnterpriseRating, name="getEnterpriseRating"),
    path('getEnterpriseRatingData/', views.getEnterpriseRatingData, name="getEnterpriseRatingData"),
    path('purchaseRatingData/', views.purchaseRatingData, name="purchaseRatingData"),
    path('test/', views.test, name="test")
]