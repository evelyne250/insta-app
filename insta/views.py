from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image,NewsLetterRecipients,Profile,Comment
from .forms import ImageForm,NewsLetterForm,CommentForm, ProfileForm
from django.contrib.auth import login, authenticate

@login_required(login_url='/accounts/login/')
def welcome(request):
    date = dt.date.today()
    images = Image.objects.all()
    user = User.objects.all()
    comment = Comment.objects.all()
    for comment_image in images:
        comments = Comment.objects.filter(comment_image=comment_image)
    # if request.method == 'POST':
    #     form = ImageForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.save()
    #         return HttpResponseRedirect('news_today')
    # else:
    #     form = ImageForm()
    return render(request, 'welcome.html', {"date": date,"user": user,"images":images,"comments":comments})


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
def profile(request, username=None):
	'''
	Method that fetches a users profile page
	'''
	current_user = request.user
	pi_images = Image.objects.filter(user=current_user)
	if not username:
         username = request.user.username
         images = Image.objects.filter(image_name=username)
	
	return render(request,"profile.html",locals(),{"pi_images":pi_images})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('profile')
    else:
        form=ProfileForm()
    return render(request,'profile_edit.html',{"form":form})


@login_required(login_url='/accounts/login/')
def search_profile(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")

        results = Profile.search_by_category(search_term)
        print(results)
        message = f"{search_term}"
        
        

        return render(request, 'search.html',{"message":message,'results': search_term})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')     
def add_comment(request,image_id):
    current_user=request.user
    if request.method=='POST':
        image_item=Image.objects.filter(id=image_id).first()
    # prof=Profile.objects.filter(user=current_user.id).first()
    # comments = Comment.objects.all()
    
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.posted_by=current_user
            comment.comment_image=image_item
            comment.save()
        return redirect('welcome')
    else:
        form=CommentForm()
    return render(request,'comment.html',{"form":form,"image_id":image_id})

