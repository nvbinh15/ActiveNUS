from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Events
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.
@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def pomodoro(request):
    return render(request, 'dashboard/pomodoro.html')

@login_required
def flashcard(request):
    return render(request, 'dashboard/flashcard.html')

@login_required
def calendar(request):
    return render(request, 'dashboard/calendar.html')
    
@login_required
def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'dashboard/calendar.html',context)

# def calendar(request):
#         from datetime import date, timedelta
#         d = date(2020, 1, 1)
#         d += timedelta(days=6 - d.weekday()) # First Sunday
#         all_sunday_in_2020 = []
#         while d.year != 2021:
#             all_sunday_in_2020.append({'name': 'my-title', 'start': d, 'end': d 
#             + timedelta(days=1)})
#             d += timedelta(days=7)
#             return render(request,'dashboard/calendar.html',{'events':all_sunday_in_2020})
@login_required
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    # return HttpResponseRedirect(reverse("calendar"))

@login_required
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)

@login_required
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)