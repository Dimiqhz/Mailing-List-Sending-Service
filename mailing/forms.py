# -*- coding: utf-8 -*-
from django import forms
from mailing.models import EmailCampaign

class EmailCampaignForm(forms.ModelForm):
    """
    Форма для создания кампании рассылки
    
    Поля:
      subject, body_html, scheduled_time
    """
    class Meta:
        model = EmailCampaign
        fields = ['subject', 'body_html', 'scheduled_time']
