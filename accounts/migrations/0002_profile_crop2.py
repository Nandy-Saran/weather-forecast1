# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-22 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='crop2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]