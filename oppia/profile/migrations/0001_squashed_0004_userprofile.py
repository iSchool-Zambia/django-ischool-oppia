# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'profile', '0001_initial'), (b'profile', '0002_auto_20151205_1345'), (b'profile', '0003_facility_type'), (b'profile', '0004_userprofile')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('district', models.ForeignKey(to='profile.District')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(to='profile.Province'),
        ),
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
        migrations.AddField(
            model_name='facility',
            name='type',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
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
