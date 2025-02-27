# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from mailing.forms import EmailCampaignForm
from mailing.models import EmailCampaign, EmailLog
from django.utils import timezone

def create_mailing(request):
    """
    Представление для создания кампании рассылки через AJAX
    
    При GET-запросе возвращает HTML-форму,
    при POST-запросе обрабатывает данные и сохраняет кампанию
    """
    if request.method == "POST" and request.is_ajax():
        form = EmailCampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            from mailing.tasks import send_email_campaign
            send_email_campaign.delay(campaign.id)
            return JsonResponse({'status': 'ok', 'campaign_id': campaign.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = EmailCampaignForm()
    return render(request, 'mailing/create_mailing.html', {'form': form})

def tracking_pixel(request, campaign_id, subscriber_email):
    """
    Представление для отслеживания открытий писем
    
    Возвращает прозрачное изображение 1x1, тем самым регистрирует факт открытия письма
    """
    log, created = EmailLog.objects.get_or_create(
        campaign_id=campaign_id,
        subscriber_email=subscriber_email
    )
    if not log.opened:
        log.opened = True
        log.open_time = timezone.now()
        log.save()
    
    # Прозрачное 1x1 GIF-изображение
    transparent_pixel = (
        "GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!"
        "\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00"
        "\x00\x02\x02D\x01\x00;"
    )
    return HttpResponse(transparent_pixel, content_type="image/gif")
