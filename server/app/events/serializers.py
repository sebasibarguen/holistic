from rest_framework import serializers
from events.models import Event, EVENT_TYPES


class EventSerializer(serializers.Serializer):

    class Meta:
        model = Event
        fields = ['message_id', 'user_id', 'event', 'type', 'properties', 'context']