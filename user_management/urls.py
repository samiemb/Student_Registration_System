from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import user_list

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('', views.front_page, name='front_page'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user_list', user_list, name='user_list'),
]