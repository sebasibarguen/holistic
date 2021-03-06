# Generated by Django 3.0.7 on 2020-06-11 19:07

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='message_id',
            new_name='messageId',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='sent_at',
            new_name='sentAt',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='userId',
        ),
        migrations.RemoveField(
            model_name='event',
            name='data',
        ),
        migrations.AddField(
            model_name='event',
            name='anonymousId',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='channel',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='integrations',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='originalTimestamp',
            field=models.DateTimeField(default='2015-02-23T22:28:55.387Z'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='receivedAt',
            field=models.DateTimeField(default='2015-02-23T22:28:55.387Z'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='version',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
