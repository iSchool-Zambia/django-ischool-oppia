# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0010_auto_20150926_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='device_id',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
