from rest_framework import serializers


from .models import Event,Reply
from profiles.serializers import UserProfileSerializer



class EventDetailSerializer(serializers.ModelSerializer):
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


class EventSerializer(serializers.ModelSerializer):
    organizer = UserProfileSerializer(read_only=True)
    number_of_likes = serializers.SerializerMethodField()
    number_of_joins = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = (
            'id',
            'organizer',
            'title',
            'description',
            'date',
            'location',
            'created_at',
            'number_of_likes',
            'number_of_joins',
        )
    def get_number_of_likes(self,instance):
        return instance.likes.count()    
    
    def get_number_of_joins(self,instance):
        return instance.users.count() 

class ReplyEventSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Reply
        fields = (
            'user',
            'event',
            'body',
            'created_at',
        )
