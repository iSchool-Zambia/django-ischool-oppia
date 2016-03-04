# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0013_auto_20151205_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='years_in_service',
        ),
    ]
