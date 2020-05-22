from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('singup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout')
]