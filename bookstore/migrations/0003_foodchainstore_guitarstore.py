# Generated by Django 4.0.1 on 2022-01-27 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_bookstore_delete_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodchainStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('food_chain', models.CharField(choices=[('jollibee', 'Jollibee'), ('chowking', 'Chowking'), ('bon chon', 'Bon Chon'), ('mcdonalds', 'McDonalds'), ('mang inasal', 'Mang Inasal')], max_length=255)),
                ('type_of_food', models.CharField(choices=[('fried chicken', 'Fried Chicken'), ('spaghetti', 'Angels and Demons'), ('burger', 'Burger'), ('fries', 'Fries'), ('sundae', 'Sundae'), ('halo halo', 'Halo Halo')], max_length=255)),
                ('is_available', models.BooleanField(default=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='GuitarStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('guitar_type', models.CharField(choices=[('electric', 'Electric'), ('acoustic', 'Acoustic'), ('bass', 'Bass'), ('ukuleles', 'Ukuleles')], max_length=255)),
                ('brand_name', models.CharField(choices=[('fender', 'Fender'), ('gretsch', 'Gretsch'), ('gibson', 'Gibson'), ('taylor', 'Taylor')], max_length=255)),
                ('is_available', models.BooleanField(default=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(max_length=255)),
                ('order_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
