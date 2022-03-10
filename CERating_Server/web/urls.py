from django.contrib import admin
from django.urls import path, include
from web.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.hello, name='index'),
    path('enterprise_login/', index.login, name="login")
]
