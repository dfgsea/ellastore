import os
from django.db import models
from datetime import date

__all__= ['ClothingStore']

class ClothingStore(models.Model):

    BRAND_CHOICES = (
        ('h&m', 'H&M'),
        ('uniqlo', 'Uniqlo'),
        ('gap', 'Gap'),
        ('levis', 'Levis'),
        ('white_off', 'White_Off'),
    )

    CLOTHES_CHOICES = (
        ('t-shirt', 'T-Shirt'),
        ('pants', 'Pants'),
        ('jackets', 'Jackets'),
        ('blouse', 'Blouse'),
    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    address = models.CharField(blank=False, max_length=255, null=False)
    brand_name = models.CharField(blank=False, max_length=255, null=False, choices=BRAND_CHOICES)
    type_of_clothes = models.CharField(blank=False, max_length=255, null=False, choices=CLOTHES_CHOICES)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        