from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'home'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]