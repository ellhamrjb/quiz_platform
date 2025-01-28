from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.start_quiz, name='start_quiz'),
    path('score/', views.view_score, name='view_score'),
]
