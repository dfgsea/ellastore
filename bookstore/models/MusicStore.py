import os
from turtle import color
from django.db import models
from datetime import date

__all__= ['MusicStore']

class MusicStore(models.Model):

    SINGER_CHOICES = (
        ('keshi', 'keshi'),
        ('lullaboy', 'lullaboy'),
        ('bruno major', 'Bruno Major'),
        ('dhruv', 'dhruv'),
        ('bruno mars', 'Bruno Mars'),
        ('post malone', 'Post Malone'),

    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    address = models.CharField(blank=False, max_length=255, null=False)
    singer_name = models.CharField(blank=False, max_length=255, null=False, choices=SINGER_CHOICES)
    album_title = models.CharField(blank=False, max_length=255, null=False)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        