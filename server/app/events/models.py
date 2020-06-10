from django.db import models

from django.contrib.postgres.fields import JSONField


EVENT_TYPES = [
    ('track', 'track'),
    ('screen', 'screen'),
    ('page', 'page'),
    ('identity', 'identity'),
]

class Event(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField()
    timestamp = models.DateTimeField()

    message_id = models.CharField(max_length=100, primary_key=True, unique=True)
    user_id = models.CharField(max_length=100, blank=True, default='')
    
    event = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=EVENT_TYPES, default='track')

    properties = JSONField()
    context = JSONField()

    data = JSONField()

    class Meta:
        ordering = ['created_at']