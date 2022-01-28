import os
from turtle import color
from django.db import models
from datetime import date

__all__= ['BagStore']

class BagStore(models.Model):

    BRAND_CHOICES = (
        ('coach', 'Coach'),
        ('kate spade', 'Kate Spade'),
        ('hermes', 'Hermes'),
        ('ysl', 'YSL'),
        ('louis vuitton', 'Louis Vuitton'),
        ('alexander mcqueen', 'Alexander McQueen'),

    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    address = models.CharField(blank=False, max_length=255, null=False)
    brand_name = models.CharField(blank=False, max_length=255, null=False, choices=BRAND_CHOICES)
    color = models.CharField(blank=False, max_length=255, null=False)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        