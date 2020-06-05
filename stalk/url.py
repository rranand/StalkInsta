from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('img', getProfile, name='profile_img'),
    url(r'^download/(?P<username>[\S]+)/$', call_download, name='downloadImg'),
]
