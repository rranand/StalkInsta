from django.db import models


class stalkers(models.Model):
    username = models.CharField(max_length=50, blank=False)
    ip = models.CharField(max_length=60, default='Unknown')
    useragent = models.CharField(max_length=100, default='Unknown')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.username


class count_views(models.Model):
    id_typ = models.CharField(max_length=10, default='views', blank=False, null=True)
    totalView = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.totalView)