from django.shortcuts import render
from .models import UploadFileForm
from news.models import Document
from mysite.settings import MEDIA_ROOT


import os
from django.http import HttpResponse, Http404

def download(request):
    s = str(request.path)
    i = s.find('/download/')
    s = s[i + 9:]
    print(s)
    file_path = MEDIA_ROOT + s
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def change(temp):
    s = temp
    s = s.split(" ")
    s = "_".join(s)
    s = s.split("(")
    s = "".join(s)
    s = s.split(")")
    s = "".join(s)
    return s

def upload_doc(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            instance = Document(file=request.FILES['file'], post=request.POST.get('title'), title=request.FILES['file'].name)
            instance.title = change(instance.title)
            instance.save()

    return render(request, 'news/posts.html', locals())