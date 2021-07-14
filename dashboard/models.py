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
    percent = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='progresses')

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


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='progress')
    completion_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.name} ({self.id})"