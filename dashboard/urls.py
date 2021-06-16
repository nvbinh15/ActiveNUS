from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pomodoro', views.pomodoro, name='pomodoro'),
    path('calendar', views.calendar, name='calendar'),
    path('flashcard', views.flashcard, name='flashcard'),
]