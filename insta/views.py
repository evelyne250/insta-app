from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image,NewsLetterRecipients,Profile
from .forms import ImageForm,NewsLetterForm
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
	'''
	Method that fetches a users profile page
	'''
	user=User.objects.all()
	images = Image.objects.all()
	profile = Profile.objects.all()
	
	return render(request,"profile.html",{"images":images,"profile":profile,"user":user})


@login_required(login_url='/accounts/login/')
def search_profile(request):

    if 'profile' in request.GET and request.GET["profile"]:
        name = request.GET.get("profile")

        results = Profile.search_by_category(search_term)
        print(results)
        message = f"{name}"
        
        

        return render(request, 'search.html',{"message":message,'results': results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})