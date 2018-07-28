# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-26 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0005_auto_20180526_1005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='user_comment',
        ),
        migrations.RemoveField(
            model_name='subredditcontent',
            name='user_comment',
        ),
        migrations.AddField(
            model_name='subredditcontent',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='reddit.Comment'),
        ),
    ]
