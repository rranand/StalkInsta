from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group


class stalkersAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip', 'datetime')
    list_filter = ('username', 'ip')
    search_fields = ('username', 'ip', 'useragent')


admin.site.register(stalkers, stalkersAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(count_views)

admin.site.site_header = 'InstaStalk'
admin.site.site_title = 'InstaStalk\'s Admin Panel'
admin.site.index_title = 'Welcome to InstaStalk'