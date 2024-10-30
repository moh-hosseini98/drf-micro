from rest_framework import serializers


from .models import Event,Reply
from profiles.serializers import UserProfileSerializer



class EventSerializer(serializers.ModelSerializer):
    organizer = UserProfileSerializer(read_only=True)
    users = UserProfileSerializer(read_only=True,many=True)
    likes = UserProfileSerializer(read_only=True,many=True)
    class Meta:
        model = Event
        fields = (
            'id',
            'organizer',
            'title',
            'description',
            'users',
            'likes',
            'date',
            'location',
            'created_at'
        )

class ReplyEventSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:

        model = Reply
        
        fields = (
            'user',
            'event',
            'body',
            'created_at',
        )
