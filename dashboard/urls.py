from django.urls import path
from django.urls import include, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pomodoro', views.pomodoro, name='pomodoro'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    path('flashcard', views.flashcard, name='flashcard'),
    path('flashcard/<int:folder_id>', views.flashcarddeck, name="flashcarddeck"),
    re_path('^calendar', views.calendar, name='calendar'),
    re_path('^add_event$', views.add_event, name='add_event'),
    re_path('^update$', views.update, name='update'),
    re_path('^remove', views.remove, name='remove'),

    # todolist
    re_path('^addtask', views.addtask, name='addtask'),
    re_path('^mark_task', views.mark_task, name='mark_task'),
    re_path('^deletetask', views.deletetask, name='deletetask'),

    # progress
    re_path('^setblue', views.setblue, name='setblue'),
    re_path('^setyellow', views.setyellow, name='setyellow'),
    re_path('^setred', views.setred, name='setred'),
    re_path('^setcream', views.setcream, name='setcream'),
    
    re_path('^increaseprogress', views.increaseprogress, name='increaseprogress'),
    re_path('^decreaseprogress', views.decreaseprogress, name='decreaseprogress'),
    re_path('^renameprogress', views.renameprogress, name='renameprogress'),
    re_path('^deleteprogress', views.deleteprogress, name='deleteprogress'),

    #flashcard
    re_path('^deletefolder', views.deletefolder, name='deletefolder'),
    re_path('^easycard$', views.easycard, name='easycard'),
    re_path('^mediumcard$', views.mediumcard, name='mediumcard'),
    re_path('^hardcard$', views.hardcard, name='hardcard'),

    #pomodoro
    re_path('^finishpomodoro', views.finishpomodoro, name='finishpomodoro'),
]