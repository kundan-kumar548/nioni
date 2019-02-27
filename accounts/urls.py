from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    url(r'signup/', views.signup, name='signup'),
    url(r'login/', views.login, name='login'),
    url(r'logout/',views.Logout, name='logout'),
]