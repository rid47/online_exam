from django.urls import path
from . import views

app_name = 'app_user'

urlpatterns = [
    path('', views.login, name='login'),
    path('login_validate/', views.login_validate, name='login_validate'),
    path('logout/', views.logout, name='logout'),

]