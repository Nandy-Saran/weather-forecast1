# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-22 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_crop2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='crop1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='crop1_set', to='datamodel.Crop'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='crop2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='crop2_set', to='datamodel.Crop'),
            preserve_default=False,
        ),
    ]