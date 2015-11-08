# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
        ('oppia', '0011_tracker_device_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='district',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='province',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.ForeignKey(default=None, blank=True, to='profile.Facility', null=True),
        ),
    ]
