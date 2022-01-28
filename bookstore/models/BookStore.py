import os
from django.db import models
from datetime import date

__all__= ['BookStore']

class BookStore(models.Model):

    AUTHOR_CHOICES = (
        ('jk rowling', 'JK Rowling'),
        ('dan brown', 'Dan Brown'),
        ('suzanne collins', 'Suzanne Collins'),
        ('john green', 'John Green'),
        ('veronica roth', 'Veronica Roth'),
        ('nicholas sparks', 'Nicholas Sparks'),
    )

    BOOKTITLE_CHOICES = (
        ('harry potter series', 'Harry Potter Series'),
        ('angels and demons', 'Angels and Demons'),
        ('the hunger games', 'The Hunger Games'),
        ('turtles all the way down', 'Turtles All the Way Down'),
        ('divergent', 'Divergent'),
        ('a walk to remember', 'A Walk to Remember'),
    )
    
    full_name = models.CharField(blank=False, max_length=255, null=False)
    author = models.CharField(blank=False, max_length=255, null=False, choices=AUTHOR_CHOICES)
    book_name = models.CharField(blank=False, max_length=255, null=False, choices=BOOKTITLE_CHOICES)
    is_available = models.BooleanField(default=False, null=False)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(default=date.today)
    

    def __str__ (self):
        return '%s'%self.full_name
        