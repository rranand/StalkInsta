from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='homepage'),
    path('img', getProfile, name='profile_img'),
]