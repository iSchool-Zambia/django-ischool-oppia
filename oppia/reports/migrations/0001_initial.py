# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import django.utils.timezone
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

        ('profile', '0003_facility_type'),
    ]

    operations = [
        migrations.CreateModel(

            name='ReportingPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('district', models.ForeignKey(default=None, blank=True, to='profile.District', null=True)),
                ('facility', models.ForeignKey(default=None, blank=True, to='profile.Facility', null=True)),
                ('province', models.ForeignKey(default=None, blank=True, to='profile.Province', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ],
        ),
        migrations.CreateModel(
            name='DashboardAccessLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created')),
                ('ip', models.GenericIPAddressField()),
                ('agent', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('data', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),

            ],
        ),
    ]
