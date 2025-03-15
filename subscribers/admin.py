# -*- coding: utf-8 -*-
from django.contrib import admin
from subscribers.models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    """
    Administrative class for Subscriber
    Allows you to conveniently manage the list of subscribers
    """
    list_display = ('id', 'first_name', 'last_name', 'email', 'birthday')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Subscriber, SubscriberAdmin)
