from django.core.serializers import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Events, Folder, Flashcard, Progress, Task, Pomodoro
from authentication.models import User
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.urls import reverse
from django import forms
from datetime import datetime, timedelta
from helpers.calendar import date_end
from supermemo2 import SMTwo, mon_day_year
from django.shortcuts import get_object_or_404



class DateInput(forms.DateInput):
    input_type = 'date'

class NameForm(forms.Form):
    prog_name = forms.CharField(label='Progress Name', max_length=100)
    start_date = forms.DateField(label='Start Date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date must be greater than start date.")

class FlashcardFolderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=100)

class NewcardForm(forms.Form):
    card_question = forms.CharField(label='Question', max_length=100)
    card_ans = forms.CharField(label='Answer', max_length=1000)


# Create your views here.
@login_required
def about(request):
    return render(request, 'dashboard/about.html')

@login_required
def account(request):
    return render(request, 'dashboard/account.html')


from json import dumps

@login_required
def home(request):
    current_user = request.user

    all_progresses = current_user.progress.all()
    progresses = []
    for progress in all_progresses:
        p = dict()
        p['id'] = progress.id
        p['title'] = progress.name
        p['count'] = progress.percent
        p['backgroundcolor'] = progress.color
        progresses.append(p)
    
    progressJSON = dumps(progresses)

    all_task = current_user.task.all()
    todolist = []
    for task in all_task:
        t = dict()
        t['label'] = task.label
        t['done'] = task.done
        t['id'] = task.id
        todolist.append(t)
    
    todoJSON = dumps(todolist)

    context = {
        "progresses": progressJSON,
        'todolist': todoJSON,
    }      

    return render(request, 'dashboard/home.html', context)

@login_required
def addtask(request):
    current_user = request.user
    label = request.GET.get("label", None)
    task = Task.objects.create(label=label, user=current_user)
    task.save
    data = {}
    return HttpResponse(data)


@login_required
def mark_task(request):
    id = request.GET.get("id", None)
    task = Task.objects.get(id=id)
    task.done = not task.done
    task.save()
    data = {}
    return HttpResponse(data)
    

@login_required
def deletetask(request):
    id = request.GET.get("id", None)
    task = Task.objects.get(id=id)
    task.delete()
    data = {}
    return HttpResponse(data)


@login_required
def pomodoro(request):
    current_user = request.user
    pomolist = current_user.pomodoro.all()
    context = {
        "pomolist": pomolist,
        "pomocount": len(pomolist)
    } 
    return render(request, 'dashboard/pomodoro.html', context)

@login_required
def finishpomodoro(request):
    current_user = request.user
    add = request.GET.get("add", None)
    if add:
        pomodoro = Pomodoro(user=current_user)
        pomodoro.save()
    data = {}
    return JsonResponse(data)

@login_required
def flashcard(request):
    current_user = request.user
    all_folder = []
    for i in current_user.flashcard_folders.all():
        no_of_cards = len(i.cards.all())
        all_folder.append((no_of_cards, i))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FlashcardFolderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            folder_name = form.cleaned_data['folder_name']
            folder = Folder(name=folder_name, user=current_user)
            folder.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('flashcard'))
            # if a GET (or any other method) we'll create a blank form
    else:
        form = FlashcardFolderForm()  
    context = {
        'form': form,
        "folders": all_folder
    }      

    return render(request, 'dashboard/flashcardfolder.html',context)



@login_required
def calendar(request):
    current_user = request.user
    all_events = current_user.events.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            prog_name = form.cleaned_data['prog_name']
            start = form.cleaned_data['start_date']
            end = date_end(form.cleaned_data['end_date'], 1)

            #SPACED REPETITION STARTS HERE#
            r = SMTwo.first_review(0, start)
            event = Events(name=prog_name, start=start, end=date_end(start,1), user=current_user)
            event.save()
            i = 0
            while True:
                if i >= 5:
                    easiness = 5
                else:
                    easiness = i+1
                r = SMTwo(r.easiness, r.interval, r.repetitions).review(easiness, start + timedelta(days=i))
                if r.review_date > end:
                    break
                event = Events(name=prog_name, start=r.review_date, end=date_end(r.review_date,1), user=current_user)
                event.save()
                i += 1

            progress = Progress(name=prog_name, percent=0, user=current_user)
            progress.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('calendar', ))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    context = {
        "events":all_events,
        'form': form
    }
    return render(request,'dashboard/calendar.html',context)


@login_required
def add_event(request):
    current_user = request.user
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end, user=current_user)
    event.save()
    data = {}
    # return HttpResponseRedirect(reverse("calendar"))

@login_required
def update(request):
    current_user = request.user
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.user = current_user
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

@login_required
def flashcarddeck(request, folder_id):
    current_user = request.user
    folder = Folder.objects.get(id=int(folder_id))
    all_cards = serializers.serialize("json", folder.cards.all(),cls=DjangoJSONEncoder)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewcardForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            question = form.cleaned_data['card_question']
            answer = form.cleaned_data['card_ans']
            card = Flashcard(question=question, answer=answer, user=current_user, folder=folder)
            card.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('flashcarddeck', args=[folder_id]))
            # if a GET (or any other method) we'll create a blank form
    else:
        form = NewcardForm()
  
    
    context = {
        'folder': folder,
        'form': form,
        "cards": all_cards
    }      

    return render(request, 'dashboard/flashcard.html',context)

@login_required
def setblue(request):
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.color = "#91b3cf"
    progress.save()
    return HttpResponse({})

@login_required
def setyellow(request):
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.color = "#fdba2e"
    progress.save()
    return HttpResponse({})

@login_required
def setred(request):
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.color = "#ff714f"
    progress.save()
    return HttpResponse({})

@login_required
def setcream(request):
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.color = "#fef4d9"
    progress.save()
    return HttpResponse({})


@login_required
def increaseprogress(request):
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.percent +=5
    progress.save()
    return HttpResponse({})    

@login_required
def decreaseprogress(request):
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.percent -=5
    progress.save()
    return HttpResponse({})

@login_required
def renameprogress(request):
    # current_user = request.user
    new_name = request.GET.get("title", None)
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.name = new_name
    progress.save()
    return HttpResponse({})

@login_required
def deleteprogress(request):
    id = request.GET.get("id", None)
    progress = Progress.objects.get(id=id)
    progress.delete()
    return HttpResponse({})

@login_required
def deletefolder(request):
    id = request.GET.get("id", None)
    folder = Folder.objects.get(id=id)
    folder.delete()
    data = {}
    return JsonResponse(data)

@login_required
def easycard(request):
    current_user = request.user
    id = request.GET.get("id", None)
    card = Flashcard.objects.get(id=id)
    card.score = (card.score * card.attempts + 5) / (card.attempts + 1)
    card.attempts += 1
    card.save()
    folder = Folder.objects.get(id=request.GET.get("folder_id", None))
    all_cards = folder.cards.all().exclude(id=id)
    all_cards = sorted(all_cards, key=lambda x: x.score, reverse=False)
    all_cards = serializers.serialize("json", all_cards,cls=DjangoJSONEncoder)
    data = {"all_cards": all_cards}
    return JsonResponse(data)

@login_required
def mediumcard(request):
    current_user = request.user
    id = request.GET.get("id", None)
    card = Flashcard.objects.get(id=id)
    card.score = (card.score * card.attempts + 2) / (card.attempts + 1)
    card.attempts += 1
    card.save()
    folder = Folder.objects.get(id=request.GET.get("folder_id", None))
    all_cards = folder.cards.all().exclude(id=id)
    all_cards = sorted(all_cards, key=lambda x: x.score, reverse=False)
    all_cards = serializers.serialize("json", all_cards,cls=DjangoJSONEncoder)
    data = {"all_cards": all_cards}
    return JsonResponse(data)

@login_required
def hardcard(request):
    current_user = request.user
    id = request.GET.get("id", None)
    card = Flashcard.objects.get(id=id)
    card.score = (card.score * card.attempts + 1) / (card.attempts + 1)
    card.attempts += 1
    card.save()
    folder = Folder.objects.get(id=request.GET.get("folder_id", None))
    all_cards = folder.cards.all().exclude(id=id)
    all_cards = sorted(all_cards, key=lambda x: x.score, reverse=False)
    all_cards = serializers.serialize("json", all_cards,cls=DjangoJSONEncoder)
    data = {"all_cards": all_cards}
    return JsonResponse(data)