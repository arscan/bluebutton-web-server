# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-24 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20161022_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='remaining_developer_invites',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='remaining_user_invites',
            field=models.IntegerField(default=0),
        ),
    ]
