from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
import requests
from .models import *
from .forms import *
from .insta_stalker import *


def home(request):
    f1 = getUsername()

    views = count_views.objects.get(id_typ='views')
    views.totalView += 1
    views.save(update_fields=['totalView'])

    context = {
        'form': f1,
    }
    return render(request, 'homepage.html', context=context)


def getProfile(request):
    f1 = getUsername()

    if request.method == 'POST':
        f1 = getUsername(request.POST)

        if f1.is_valid():
            username = f1.cleaned_data['username']
            s = stalkers.objects.create(username=username, ip=str(request.META['REMOTE_ADDR']),
                                        useragent=request.META['HTTP_USER_AGENT'])
            s.save()

            if username in not_allowed:
                context = {
                    'message': 'You are not allowed to see admin\'s Profile',
                    'form': f1,
                }
            else:
                res = get_image(username)

                if res == -1:
                    context = {
                        'message': 'No, User associated with ' + str(username),
                        'form': f1,
                    }
                else:
                    context = {
                        'image': str(res),
                        'username': username,
                        'form': f1,
                    }
        else:
            context = {
                'message': 'Invalid Input Given',
                'form': f1,
            }
    else:
        return render(request, 'homepage.html', context={'form': f1})

    return render(request, 'result.html', context)


def call_download(request, link):

    if len(link) != 0:
        response = HttpResponse(requests.get(link).content, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % 'Image.jpg'
        response['X-Sendfile'] = link

        return response
    return HttpResponseRedirect(reverse('homepage'))


def error_page(request, found):
    return HttpResponseRedirect(reverse('homepage'))
