# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_auto_20160819_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='assets'),
        ),
    ]
