from rest_framework import serializers
from events.models import Event, EVENT_TYPES


class EventSerializer(serializers.Serializer):
    message_id = serializers.CharField(max_length=100, required=True, allow_blank=False)
    user_id = serializers.CharField(max_length=100, allow_blank=True, default='')
    
    event = serializers.CharField(required=False, allow_blank=True, max_length=100)
    type = serializers.ChoiceField(choices=EVENT_TYPES, default='track')

    properties = serializers.JSONField()
    context = serializers.JSONField()

    data = serializers.JSONField()

    def create(self, validated_data):
        """
        Create and return a new `Event` instance, given the validated data.
        """
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Event` instance, given the validated data.
        """
        instance.event = validated_data.get('event', instance.event)
        instance.type = validated_data.get('type', instance.type)
        instance.properties = validated_data.get('properties', instance.properties)
        instance.context = validated_data.get('context', instance.context)
        instance.save()
        return instance