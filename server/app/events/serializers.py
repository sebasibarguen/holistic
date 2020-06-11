from rest_framework import serializers
from events.models import Event, EVENT_TYPES


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'created_at', 
            'messageId', 
            'userId', 
            'event', 
            'type', 
            'properties', 
            'context', 
            'sentAt',
            'timestamp',
            'originalTimestamp'
        ]