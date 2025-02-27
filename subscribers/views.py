# -*- coding: utf-8 -*-
from django.shortcuts import render
from subscribers.models import Subscriber

def subscriber_list(request):
    """
    Представление для отображения списка подписчиков
    """
    subscribers = Subscriber.objects.all()
    return render(request, 'subscribers/subscriber_list.html', {'subscribers': subscribers})
