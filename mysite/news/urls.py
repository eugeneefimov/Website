
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from news.models import Document
from . import views
from mysite.settings import MEDIA_ROOT

urlpatterns = [

    url(r'^list/$', ListView.as_view(queryset=Document.objects.all().order_by("-date")[:20],
                                    template_name="news/PostList.html")),

    url(r'^$', views.upload_doc, name='upload_doc'),

    url(r'^list/(?P<pk>\d+)$', DetailView.as_view(model = Document, template_name = "news/post.html"), {'document root': MEDIA_ROOT}),

    url(r'^list/download/', views.download),
]
