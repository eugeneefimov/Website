from django.db import models
from django import forms
from mysite.settings import MEDIA_ROOT
from datetime import datetime


class Document(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    file = models.FileField()
    address = models.TextField(default=MEDIA_ROOT)

    def __str__(self):
        return self.title

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()