from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image,NewsLetterRecipients,Profile
from .forms import NewImageForm,NewsLetterForm,UpdateUserForm,UpdateUserProfileForm
from django.contrib.auth import login, authenticate

def welcome(request):
    date = dt.date.today()
    images = Image.objects.all()
    user = User.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()


            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(request, 'welcome.html', {"date": date,"user": user,"images":images,"letterForm":form})

# @login_required(login_url='/accounts/login/')
# def home(request):
#     images = Image.objects.all()
#     return render(request, 'home.html', {"images":images})


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


# @login_required(login_url='login')
# def profile(request):
#     images = Profile.objects.all()
#     current_user = request.user
#     if request.method == 'POST':
#         prof_form = ProfileForm(request.POST, request.FILES)
#         if prof_form.is_valid() :
#             profile = prof_form.save(commit=False)
#             profile.user = current_user
#             profile.save()
            
#             return HttpResponseRedirect('welcome')
#     else:
#         prof_form = ProfileForm()
  
#     return render(request, 'profile.html', {'prof_form': prof_form,'images': images})

@login_required(login_url='/accounts/login/')
def profile(request):
    prof = Profile.objects.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'prof': prof,

    }
    return render(request, 'profile.html', params)

