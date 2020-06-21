from django import forms
from .models import Video
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(label='Email', max_length=20)


class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
    #video = forms.IntegerField(widget=forms.HiddenInput(), initial=1)


class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'videofile', 'user']


print('Video.objects')
