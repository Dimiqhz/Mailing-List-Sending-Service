# -*- coding: utf-8 -*-
from django.db import models

class Subscriber(models.Model):
    """
    Модель подписчика
    
    Поля:
      first_name (str): имя подписчика
      last_name (str): фамилия подписчика
      email (str): адрес электронной почты подписчика
      birthday (date): дата рождения подписчика
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True)
    
    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
