from authentication.models import User
from django.db import models
from authentication.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='events')

    def __str__(self):
        return f"{self.name} ({self.id})"

class Progress(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    percent = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True, default=0)
    color = models.CharField(max_length=7, default='#ffffff', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='progress')

    def __str__(self):
        return f"{self.name} ({self.id})"

class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='flashcard_folders')
    
    def __str__(self):
        return f"{self.name} ({self.id})"

class Flashcard(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255,null=True,blank=True)
    answer = models.CharField(max_length=1000,null=True,blank=True)
    startcard = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, related_name='cards')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='cards')
    score = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} ({self.id})"


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=200)
    done = models.BooleanField(null=True, blank=True, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='task')

    def __str__(self):
        return f"{self.label} ({self.id})"

class Pomodoro(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='pomodoro')

    def __str__(self):
        return f"{self.user}"