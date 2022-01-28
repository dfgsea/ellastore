import os
from django.db import models
from datetime import date

__all__= ['GuitarStore']

class GuitarStore(models.Model):

    GUITAR_CHOICES = (
        ('electric', 'Electric'),
        ('acoustic', 'Acoustic'),
        ('bass', 'Bass'),
        ('ukuleles', 'Ukuleles'),
    )

    BRAND_CHOICES = (
        ('fender', 'Fender'),
        ('gretsch', 'Gretsch'),
        ('gibson', 'Gibson'),
        ('taylor', 'Taylor')


    )
    full_name = models.CharField(blank=False, max_length=255, null=False)
    guitar_type = models.CharField(blank=False, max_length=255, null=False, choices=GUITAR_CHOICES)
    brand_name = models.CharField(blank=False, max_length=255, null=False, choices=BRAND_CHOICES)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    color = models.CharField(blank=False, max_length=255, null=False)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
