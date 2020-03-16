from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login_view/', views.user_login_view, name='user_login_view'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register'),
]
