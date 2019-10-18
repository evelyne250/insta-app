from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Image
from .forms import NewImageForm

def welcome(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'welcome.html', {"date": date,"images":images})

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images":images})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})