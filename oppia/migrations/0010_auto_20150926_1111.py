# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0009_auto_20150524_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='district',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='facility',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profession',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='province',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='years_in_service',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
