# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-26 10:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0004_auto_20180526_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subredditcontent',
            old_name='comment',
            new_name='user_comment',
        ),
    ]