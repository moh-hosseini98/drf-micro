from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):

    class Gender(models.TextChoices):

        MALE = (
            "male",
            _("Male"),
        )
        FEMALE = (
            "female",
            _("Female"),
        )
        OTHER = (
            "other",
            _("Other"),
        )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    bio = models.TextField(max_length=1024,blank=True)
    gender = models.CharField(
        max_length=6,
        choices=Gender,
        default=Gender.OTHER
    )

    def __str__(self):
        return self.user.email
    


