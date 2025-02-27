# -*- coding: utf-8 -*-
from django.contrib import admin
from subscribers.models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    """
    Административный класс для Subscriber
    Позволяет удобно управлять списком подписчиков
    """
    list_display = ('id', 'first_name', 'last_name', 'email', 'birthday')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Subscriber, SubscriberAdmin)
