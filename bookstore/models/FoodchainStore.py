import os
from django.db import models
from datetime import date

__all__= ['FoodchainStore']

class FoodchainStore(models.Model):

    FOODCHAIN_CHOICES = (
        ('jollibee', 'Jollibee'),
        ('chowking', 'Chowking'),
        ('bon chon', 'Bon Chon'),
        ('mcdonalds', 'McDonalds'),
        ('mang inasal', 'Mang Inasal'),
    )

    FOOD_CHOICES = (
        ('fried chicken', 'Fried Chicken'),
        ('spaghetti', 'Angels and Demons'),
        ('burger', 'Burger'),
        ('fries', 'Fries'),
        ('sundae', 'Sundae'),
        ('halo halo', 'Halo Halo'),
    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    address = models.CharField(blank=False, max_length=255, null=False)
    food_chain = models.CharField(blank=False, max_length=255, null=False, choices=FOODCHAIN_CHOICES)
    type_of_food = models.CharField(blank=False, max_length=255, null=False, choices=FOOD_CHOICES)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        