import os
from turtle import color
from django.db import models
from datetime import date

__all__= ['SneakersStore']

class SneakersStore(models.Model):

    BRAND_CHOICES = (
        ('adidas', 'Adidas'),
        ('nike', 'Nike'),
        ('reebok', 'Reebok'),
        ('converse', 'Converse'),
        ('vans', 'Vans'),
        ('puma', 'Puma'),

    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    address = models.CharField(blank=False, max_length=255, null=False)
    brand_name = models.CharField(blank=False, max_length=255, null=False, choices=BRAND_CHOICES)
    size = models.IntegerField(null=True, blank=True)
    color = models.CharField(blank=False, max_length=255, null=False)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        