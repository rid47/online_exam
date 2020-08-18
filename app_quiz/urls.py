from django.urls import path
from . import views

app_name = 'app_quiz'

urlpatterns = [
    path('question/', views.question, name='question'),

]
