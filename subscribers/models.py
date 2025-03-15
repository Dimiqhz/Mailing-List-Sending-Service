# -*- coding: utf-8 -*-
from django.db import models

class Subscriber(models.Model):
    """
    Subscriber Model
    
    Fields:
      first_name (str): subscriber's first name
      last_name (str): subscriber's last name
      email (str): subscriber's email address
      birthday (date): subscriber's date of birth
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.email)
