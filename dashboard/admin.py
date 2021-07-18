from django.contrib import admin
from .models import Events, Folder, Flashcard, Task, Pomodoro

# Register your models here.
# admin.site.register(Events)
# admin.site.register(Folder)
# admin.site.register(Flashcard)

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'start', 'end']


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'description']

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'folder', 'user']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'completion_level']

@admin.register(Pomodoro)
class PomodoroAdmin(admin.ModelAdmin):
    list_display = ['user']
    

