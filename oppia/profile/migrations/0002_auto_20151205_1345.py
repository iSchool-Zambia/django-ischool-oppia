# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name': 'Facility', 'verbose_name_plural': 'facilities'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': 'Province', 'verbose_name_plural': 'Provinces'},
        ),
        migrations.AddField(
            model_name='facility',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='code',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
    ]
