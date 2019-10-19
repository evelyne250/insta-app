from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image,NewsLetterRecipients,Profile
from .forms import ImageForm,NewsLetterForm,UpdateUserForm,UpdateUserProfileForm
from django.contrib.auth import login, authenticate

@login_required(login_url='/accounts/login/')
def welcome(request):
    date = dt.date.today()
    images = Image.objects.all()
    user = User.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('news_today')
    else:
        form = ImageForm()
    return render(request, 'welcome.html', {"date": date,"user": user,"images":images,"form":form})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')

    else:
        form = ImageForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    prof = Profile.objects.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm()
        prof_form = UpdateUserProfileForm()
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'prof': prof,

    }
    return render(request, 'profile.html', params)

