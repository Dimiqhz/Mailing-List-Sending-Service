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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.email)
