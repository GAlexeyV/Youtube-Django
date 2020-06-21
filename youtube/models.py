from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Video(models.Model):
#    description = models.TextField(max_length=300)
#    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
#    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#    video = models.FileField(blank=False, null=False)

#    def __str__(self):
#        return self.title

#    def delete(self, *args, **kwargs):
#        self.video.delete()
#        super().delete(*args, **kwargs)


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    videofile = models.FileField(upload_to='videos', null=True, verbose_name="")

    def __str__(self):
        return self.title + ": " + str(self.videofile)


class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
