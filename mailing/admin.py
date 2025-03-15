# -*- coding: utf-8 -*-
from django.contrib import admin
from mailing.models import EmailCampaign, EmailLog

class EmailCampaignAdmin(admin.ModelAdmin):
    """
    Administrative classroom for EmailCampaign
    """
    list_display = ('id', 'subject', 'scheduled_time', 'is_sent', 'created_at')
    list_filter = ('is_sent', 'created_at')
    search_fields = ('subject',)

class EmailLogAdmin(admin.ModelAdmin):
    """
    Displays information about each email opening
    """
    list_display = ('id', 'campaign', 'subscriber_email', 'opened', 'open_time')
    list_filter = ('opened', 'open_time')
    search_fields = ('subscriber_email',)

admin.site.register(EmailCampaign, EmailCampaignAdmin)
admin.site.register(EmailLog, EmailLogAdmin)
