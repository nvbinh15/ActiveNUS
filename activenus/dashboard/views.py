from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def pomodoro(request):
    return render(request, 'dashboard/pomodoro.html')