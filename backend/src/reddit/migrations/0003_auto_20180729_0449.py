# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-07-29 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0002_auto_20180729_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subreddit_content',
        ),
        migrations.AddField(
            model_name='subredditcontent',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='reddit.Comment'),
        ),
    ]
