import os
from turtle import color
from django.db import models
from datetime import date

__all__= ['KpopStore']

class KpopStore(models.Model):

    KPOPSINGER_CHOICES = (
        ('bts', 'BTS'),
        ('twice', 'Twice'),
        ('blackpink', 'Blackpink'),
        ('txt', 'TXT'),
        ('exo', 'EXO'),
        ('stray kids', 'Stray Kids'),

    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    address = models.CharField(blank=False, max_length=255, null=False)
    singer_name = models.CharField(blank=False, max_length=255, null=False, choices=KPOPSINGER_CHOICES)
    album_title = models.CharField(blank=False, max_length=255, null=False)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        