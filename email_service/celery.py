# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Устанавливаем модуль настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_service.settings')

# Создаем экземпляр Celery
app = Celery('email_service')

# Загружаем настройки Django (для Celery 3.x не используется параметр namespace)
app.config_from_object('django.conf:settings')

# Автоматически обнаруживаем задачи в приложениях, указанных в INSTALLED_APPS
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
