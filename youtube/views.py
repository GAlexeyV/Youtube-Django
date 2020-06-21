from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, CommentForm, UploadVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView, CreateView
from .models import Video, Comment
import string
import random
from django.core.files.storage import FileSystemStorage
import os
from wsgiref.util import FileWrapper
from django.urls import reverse_lazy

# Create your views here.


class HomeView(View):
    template_name = 'youtube/home.html'

    def get(self, request):
        # fetch video from DB
        most_recent_videos = Video.objects.order_by('-datetime')[:8]

        return render(request, self.template_name, {'menu_active_item': 'home',
                                                    'most_recent_videos': most_recent_videos})


class RegisterView(View):
    template_name = 'youtube/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('Already registered. Redirecting.')
            print(request.user)
            return HttpResponseRedirect('/')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to RegisterForm()
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create a User account
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login/')
        return HttpResponse('This is Register view. POST Request.')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class CommentView(View):
    template_name = 'youtube/comment.html'

    def post(self, request):
        # pass filled out HTML-Form from View to CommentForm()
        form = CommentForm(request.POST)
        if form.is_valid():
            # create a Comment DB Entry
            text = form.cleaned_data['text']
            video_id = request.POST['videofile']
            video = Video.objects.get(id=videofile_id)

            new_comment = Comment(text=text, user=request.user, video=video)
            new_comment.save()
            return HttpResponseRedirect('/video_list/{}'.format(str(video_id)))
        return HttpResponse('This is Register view. POST Request.')


def delete_video(request, pk):
    if request.method == 'POST':
        video = Vidoe.objects.get(pk=pk)
        video.delete()
    return redirect('video_list')


def upload_video(request):

    videofile = Video.objects.all()

    form = UploadVideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'videofile': videofile,
               'form': form
               }

    return render(request, 'youtube/upload_video.html', context)


class VideoList(ListView):
    model = Video
    template_name = 'youtube/video_list.html'
