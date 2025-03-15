# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class EmailCampaign(models.Model):
    """
    A model describing a mailing campaign.
    
    Fields:
      subject (str): subject of the email.
      body_html (str): The HTML template of the email, which may use variables (e.g. {{ first_name }})
      scheduled_time (datetime): the time scheduled to be sent.
      is_sent (bool): flag indicating whether the mailing has been sent or not
      created_at (datetime): time when the campaign was created
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
