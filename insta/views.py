from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Image

def welcome(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'welcome.html', {"date": date,"images":images})

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images":images})
