import os
from turtle import color
from django.db import models
from datetime import date

__all__= ['ArtStore']

class ArtStore(models.Model):

    ARTIST_CHOICES = (
        ('leonardo da vinci', 'Leonardo da Vinci'),
        ('vincent van gogh', 'Vincent Van Gogh'),
        ('johannes vermeer', 'Johannes Vermeer'),
        ('pablo picasso', 'Pablo Picasso'),
        ('gustav klimt', 'Gustav Klimt'),
        ('edvard munch', 'Edvard Munch'),

    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    address = models.CharField(blank=False, max_length=255, null=False)
    artist_name = models.CharField(blank=False, max_length=255, null=False, choices=ARTIST_CHOICES)
    art_title = models.CharField(blank=False, max_length=255, null=False)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        