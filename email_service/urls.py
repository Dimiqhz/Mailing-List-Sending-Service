# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mailing/', include('mailing.urls')),
    url(r'^subscribers/', include('subscribers.urls')),
]
