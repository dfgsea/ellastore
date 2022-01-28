import os
from turtle import color
from django.db import models
from datetime import date

__all__= ['CarStore']

class CarStore(models.Model):

    BRAND_CHOICES = (
        ('audi', 'Audi'),
        ('bmw', 'BMW'),
        ('bentley', 'Bentley'),
        ('ferrari', 'Ferrari'),
        ('lamborghini', 'Lamborghini'),
        ('porsche', 'Porsche'),

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
        