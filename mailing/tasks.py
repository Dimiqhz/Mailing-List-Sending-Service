# -*- coding: utf-8 -*-
from celery import task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from mailing.models import EmailCampaign
from subscribers.models import Subscriber
from django.utils import timezone
from django.template import Template, Context
import logging

@task
def send_email_campaign(campaign_id):
    """
    Задача Celery для отправки рассылки

    Получает кампанию по id, рендерит HTML-макет с переменными для каждого активного подписчика,
    добавляет ссылку для отписки и отправляет email. 
    
    В случае ошибок логирует их

    :param campaign_id: int - идентификатор кампании рассылки
    """
    try:
        campaign = EmailCampaign.objects.get(id=campaign_id)
    except EmailCampaign.DoesNotExist:
        logging.error("Кампания с id %s не найдена." % campaign_id)
        return

    subscribers = Subscriber.objects.filter(is_active=True)
    
    for subscriber in subscribers:
        context = {
            'first_name': subscriber.first_name,
            'last_name': subscriber.last_name,
            'birthday': subscriber.birthday.strftime('%d.%m.%Y') if subscriber.birthday else '',
        }
        t = Template(campaign.body_html)
        rendered_body = t.render(Context(context))

        unsubscribe_url = "http://127.0.0.1:8000/subscribers/unsubscribe/{}/".format(subscriber.email)
        rendered_body += u'<p><a href="{}">Отписаться от рассылки</a></p>'.format(unsubscribe_url)
        
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com')
        subject = campaign.subject
        to_email = subscriber.email
        
        msg = EmailMultiAlternatives(
            subject=subject,
            body=rendered_body,
            from_email=from_email,
            to=[to_email]
        )
        msg.encoding = 'utf-8'
        msg.attach_alternative(rendered_body, "text/html")
        
        try:
            msg.send()
            logging.info("Email отправлен на: {}".format(to_email))
        except Exception as e:
            logging.error("Ошибка отправки email на {}: {}".format(to_email, e))
    
    campaign.is_sent = True
    campaign.save()
