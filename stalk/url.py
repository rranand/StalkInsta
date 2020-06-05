from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('img', getProfile, name='profile_img'),
    url(r'^download/(?P<link>[\S]*)/$', call_download, name='downloadImg'),
    url(r'(?P<found>[\S]+)/$', error_page, name='error_404'),
]
