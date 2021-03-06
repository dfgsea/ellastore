# Generated by Django 4.0.1 on 2022-01-27 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_artstore_carstore_musicstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='BagStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('brand_name', models.CharField(choices=[('coach', 'Coach'), ('kate spade', 'Kate Spade'), ('hermes', 'Hermes'), ('ysl', 'YSL'), ('louis vuitton', 'Louis Vuitton'), ('alexander mcqueen', 'Alexander McQueen')], max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='KpopStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('singer_name', models.CharField(choices=[('bts', 'BTS'), ('twice', 'Twice'), ('blackpink', 'Blackpink'), ('txt', 'TXT'), ('exo', 'EXO'), ('stray kids', 'Stray Kids')], max_length=255)),
                ('album_title', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
