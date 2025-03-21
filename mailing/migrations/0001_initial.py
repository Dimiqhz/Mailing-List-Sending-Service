# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2025-02-27 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body_html', models.TextField()),
                ('scheduled_time', models.DateTimeField()),
                ('is_sent', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_email', models.EmailField(max_length=254)),
                ('opened', models.BooleanField(default=False)),
                ('open_time', models.DateTimeField(blank=True, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.EmailCampaign')),
            ],
        ),
    ]
