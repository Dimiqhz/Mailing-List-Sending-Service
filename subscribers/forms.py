# -*- coding: utf-8 -*-
from django import forms
from subscribers.models import Subscriber
import bleach

class SubscriberForm(forms.ModelForm):
    """
    Newsletter subscription form
    
    Fields: first name, last name, email, date of birth
    """
    class Meta:
        model = Subscriber
        fields = ['first_name', 'last_name', 'email', 'birthday']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return bleach.clean(first_name, tags=[], strip=True)
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return bleach.clean(last_name, tags=[], strip=True)
