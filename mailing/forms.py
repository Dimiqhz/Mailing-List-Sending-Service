# -*- coding: utf-8 -*-
from django import forms
from mailing.models import EmailCampaign
import bleach
from django.utils import timezone

class EmailCampaignForm(forms.ModelForm):
    """
    Форма для создания кампании рассылки
    
    Поля: subject, body_html, scheduled_time
    """
    class Meta:
        model = EmailCampaign
        fields = ['subject', 'body_html', 'scheduled_time']

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        clean_subject = bleach.clean(subject, tags=[], strip=True)
        return clean_subject

    def clean_body_html(self):
        body_html = self.cleaned_data.get('body_html')
        allowed_tags = ['p', 'a', 'b', 'i', 'u', 'strong', 'em', 'br']
        clean_body = bleach.clean(body_html, tags=allowed_tags, strip=True)
        return clean_body

    def clean_scheduled_time(self):
        scheduled_time = self.cleaned_data.get('scheduled_time')
        if scheduled_time < timezone.now():
            raise forms.ValidationError("Время отправки должно быть в будущем.")
        return scheduled_time
