from django.shortcuts import render, redirect
import datetime as dt
from .models import Image
def welcome(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'welcome.html', {"date": date,"images":images})
