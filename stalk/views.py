from django.shortcuts import render
from .models import *
from .forms import *
from .insta_stalker import get_image


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

    if request.method == 'POST' and request.is_ajax():
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
                        'message': 'Something Went Wrong Please Try Again',
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
