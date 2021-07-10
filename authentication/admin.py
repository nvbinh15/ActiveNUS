from django.contrib import admin
from .models import User
from dashboard.models import Events, Folder, Flashcard
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Events)
admin.site.register(Folder)
admin.site.register(Flashcard)