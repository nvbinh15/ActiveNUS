from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_user, name='auth_login'),
    path('', views.login_user, name='auth_login'),
    path('register', views.register, name='auth_register'),
    path("logout_user", views.logout_user, name='logout_user'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
]