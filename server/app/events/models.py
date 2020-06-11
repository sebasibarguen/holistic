from django.db import models

from django.contrib.postgres.fields import JSONField


EVENT_TYPES = [
    ('track', 'track'),
    ('screen', 'screen'),
    ('page', 'page'),
    ('identity', 'identity'),
]

class Event(models.Model):

    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    
    timestamp = models.DateTimeField()
    receivedAt = models.DateTimeField(blank=True, null=True)
    sentAt = models.DateTimeField(blank=True, null=True)
    originalTimestamp = models.DateTimeField(blank=True, null=True)

    messageId = models.CharField(max_length=100, primary_key=True, unique=True)
    userId = models.CharField(max_length=100, blank=True, default='')
    anonymousId = models.CharField(max_length=100, blank=True, default='')
    
    event = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=EVENT_TYPES, default='track')

    version = models.CharField(max_length=100, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    properties = JSONField(blank=True, null=True)
    integrations = JSONField(blank=True, null=True)
    context = JSONField(blank=True)

    class Meta:
        ordering = ['created_at']