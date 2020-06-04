from django.contrib import admin
from django.urls import path, include
from stalk import url


urlpatterns = [
    path('papa/', admin.site.urls),
    path('', include(url)),
]
