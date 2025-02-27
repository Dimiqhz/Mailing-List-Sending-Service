# -*- coding: utf-8 -*-
from celery import task
from django.core.mail import EmailMultiAlternatives
from mailing.models import EmailCampaign
from subscribers.models import Subscriber
import logging
from django.utils import timezone
from django.template import Template, Context

@task
def send_email_campaign(campaign_id):
    """
    Task Celery для отправки рассылки
    
    :param campaign_id: int — идентификатор кампании рассылки
    """
    try:
        campaign = EmailCampaign.objects.get(id=campaign_id)
    except EmailCampaign.DoesNotExist:
        logging.error("Кампания с id %s не найдена." % campaign_id)
        return

    subscribers = Subscriber.objects.all()
    
    for subscriber in subscribers:
        context = {
            'first_name': subscriber.first_name,
            'last_name': subscriber.last_name,
            'birthday': subscriber.birthday.strftime('%d.%m.%Y') if subscriber.birthday else '',
        }
        t = Template(campaign.body_html)
        rendered_body = t.render(Context(context))
        
        tracking_url = "http://localhost/mailing/tracking/{campaign_id}/{email}/".format(
            campaign_id=campaign.id,
            email=subscriber.email
        )
        # Пиксель для отслеживания открытия письма
        rendered_body += '<img src="%s" width="1" height="1" alt=""/>' % tracking_url
        
        msg = EmailMultiAlternatives(
            subject=campaign.subject,
            body=rendered_body, 
            to=[subscriber.email]
        )
        msg.attach_alternative(rendered_body, "text/html")
        msg.send()

    campaign.is_sent = True
    campaign.save()