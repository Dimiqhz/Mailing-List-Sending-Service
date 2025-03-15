# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from mailing.forms import EmailCampaignForm
from mailing.models import EmailCampaign, EmailLog
from django.utils import timezone

def create_campaign(request):
    """
    View for creating a mailing campaign via AJAX
    
    At GET-request returns HTML-form,
    at POST request processes the data and saves the campaign
    """
    if request.method == "POST" and request.is_ajax():
        form = EmailCampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            from mailing.tasks import send_email_campaign
            if campaign.scheduled_time > timezone.now():
                send_email_campaign.apply_async(args=[campaign.id], eta=campaign.scheduled_time)
            else:
                send_email_campaign.delay(campaign.id)
            return JsonResponse({'status': 'ok', 'campaign_id': campaign.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = EmailCampaignForm()
    return render(request, 'mailing/create_campaign.html', {'form': form})

def tracking_pixel(request, campaign_id, subscriber_email):
    """
    View for tracking email openings
    
    Returns a 1x1 transparent image, thereby registering the fact that a letter has been opened
    """
    log, created = EmailLog.objects.get_or_create(
        campaign_id=campaign_id,
        subscriber_email=subscriber_email
    )
    if not log.opened:
        log.opened = True
        log.open_time = timezone.now()
        log.save()
    
    # 1х1 GIF
    transparent_pixel = (
        "GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!"
        "\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00"
        "\x00\x02\x02D\x01\x00;"
    )
    return HttpResponse(transparent_pixel, content_type="image/gif")

def campaign_list(request):
    """
    A view for displaying a list of mailing campaigns.
    """
    campaigns = EmailCampaign.objects.all().order_by('-created_at')
    return render(request, 'mailing/campaign_list.html', {'campaigns': campaigns})

def email_logs(request):
    """
    A view for displaying logs of email openings.
    """
    logs = EmailLog.objects.all().order_by('-open_time')
    return render(request, 'mailing/email_logs.html', {'logs': logs})