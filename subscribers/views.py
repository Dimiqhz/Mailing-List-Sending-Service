# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from subscribers.models import Subscriber
from subscribers.forms import SubscriberForm

def subscriber_list(request):
    """
    Представление для отображения списка подписчиков
    """
    subscribers = Subscriber.objects.all()
    return render(request, 'subscribers/subscriber_list.html', {'subscribers': subscribers})

def subscribe(request):
    """
    Представление для обработки подписки пользователя
    При GET-запросе отображается форма подписки,
    при POST-запросе данные формы сохраняются, и показывается страница с подтверждением
    """
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'subscribers/subscribe_success.html')
    else:
        form = SubscriberForm()
    return render(request, 'subscribers/subscribe.html', {'form': form})

def unsubscribe(request, email):
    """
    Представление для отписки подписчика от рассылки
    """
    subscriber = get_object_or_404(Subscriber, email=email)
    if request.method == "POST":
        subscriber.is_active = False
        subscriber.save()
        return render(request, 'subscribers/unsubscribe_success.html', {'email': email})
    return render(request, 'subscribers/unsubscribe_confirm.html', {'email': email})
