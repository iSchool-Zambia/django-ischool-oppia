# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20151205_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='type',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
    ]
