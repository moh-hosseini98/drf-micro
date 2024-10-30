from django.db import models
from profiles.models import Profile


class Event(models.Model):
    organizer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='user_events'
    )

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024,blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255,default="Iran,Tehran",blank=True)
    users = models.ManyToManyField(
        Profile,
        blank=True,
        related_name="users"
    )

    likes = models.ManyToManyField(
        Profile,
        blank=True,
        related_name="likes"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    
    body = models.TextField(max_length=1024)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.first_name