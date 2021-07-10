from authentication.models import User
from django.db import models
from authentication.models import User

# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='events')

    def __str__(self):
        return self.name

class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='flashcard_folders')

class Flashcard(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255,null=True,blank=True)
    answer = models.CharField(max_length=1000,null=True,blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, related_name='cards')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='cards')
