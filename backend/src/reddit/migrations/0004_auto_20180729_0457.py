# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-07-29 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0003_auto_20180729_0449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subredditcontent',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='subreddit_content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subreddit_content', to='reddit.SubredditContent'),
        ),
    ]
