from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom users model"""

    # User fields
    email = models.EmailField(verbose_name=_("email address"), db_index=True, unique=True)
    first_name = models.CharField(verbose_name=_("first name"), max_length=50)
    last_name = models.CharField(verbose_name=_("last name"), max_length=50)

    # User permissions
    is_staff = models.BooleanField(default=False)  # For admin access
    is_active = models.BooleanField(default=True)  # For users activation

    # Timestamps
    date_joined = models.DateTimeField(default=timezone.now)


    REQUIRED_FIELDS = ['first_name','last_name']

    USERNAME_FIELD = "email"

    objects = CustomUserManager()


    def __str__(self):
        """String representation of the user."""
        return self.email