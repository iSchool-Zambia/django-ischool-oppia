# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_squashed_0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='years_in_service',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='service_entry_date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
