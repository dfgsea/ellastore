from django.conf import settings

from django.db import migrations, models

import django.db.models.deletion




class Migration(migrations.Migration):



    initial = True



    dependencies = [

    ]



    operations = [

        migrations.CreateModel(

            name='count',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('stock', models.IntegerField()),

            ],

        ),

    ]