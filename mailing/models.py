# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class EmailCampaign(models.Model):
    """
    Модель, описывающая кампанию рассылки.
    
    Поля:
      subject (str): тема письма.
      body_html (str): HTML-шаблон письма, в котором могут использоваться переменные (например, {{ first_name }})
      scheduled_time (datetime): время, запланированное для отправки
      is_sent (bool): флаг, указывающий, отправлена ли рассылка
      created_at (datetime): время создания кампании
    """
    subject = models.CharField(max_length=255)
    body_html = models.TextField()
    scheduled_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.subject


class EmailLog(models.Model):
    """
    Модель для отслеживания открытий писем
    
    Поля:
      campaign (ForeignKey): связь с EmailCampaign
      subscriber_email (str): email подписчика
      opened (bool): флаг, указывающий, что письмо открыто
      open_time (datetime): время открытия письма
    """
    campaign = models.ForeignKey(EmailCampaign, on_delete=models.CASCADE)
    subscriber_email = models.EmailField()
    opened = models.BooleanField(default=False)
    open_time = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return u"Log: %s - %s" % (self.subscriber_email, self.campaign.subject)
