from django.urls import path
from django.urls import include, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pomodoro', views.pomodoro, name='pomodoro'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    # path('calendar', views.calendar, name='calendar'),
    path('flashcard', views.flashcard, name='flashcard'),
    path('flashcard/<int:folder_id>', views.flashcarddeck, name="flashcarddeck"),
    re_path('^calendar', views.calendar, name='calendar'),
    re_path('^add_event$', views.add_event, name='add_event'),
    re_path('^update$', views.update, name='update'),
    re_path('^remove', views.remove, name='remove'),

    # flashcards
    re_path('^add_task', views.add_task, name='add_task'),
    re_path('^mark_task', views.mark_task, name='mark_task'),
    re_path('^remove_task', views.remove_task, name='remove_task'),
]