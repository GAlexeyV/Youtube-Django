"""dj_youtube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from youtube.views import HomeView, RegisterView, LogoutView, CommentView, VideoList
from youtube.views import delete_video, upload_video as View
from youtube import views as youtube_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('upload_video/', youtube_views.upload_video, name='upload_video'),
    path('login/', auth_views.LoginView.as_view(template_name='youtube/login.html'), name='login'),
    path('register/', RegisterView.as_view()),
    path('comment/', CommentView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('video_list/', VideoList.as_view(), name='video_list'),
    path('video/<int:pk>/', youtube_views.delete_video, name='delete_video'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
