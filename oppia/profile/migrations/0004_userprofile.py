# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0003_facility_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about', models.TextField(default=None, null=True, blank=True)),
                ('can_upload', models.BooleanField(default=False)),
                ('job_title', models.TextField(default=None, null=True, blank=True)),
                ('organisation', models.TextField(default=None, null=True, blank=True)),
                ('phone_number', models.TextField(default=None, null=True, blank=True)),
                ('profession', models.TextField(default=None, null=True, blank=True)),
                ('years_in_service', models.TextField(default=None, null=True, blank=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='profile.Facility', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
