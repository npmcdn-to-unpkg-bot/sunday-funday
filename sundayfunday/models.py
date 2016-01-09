from django.contrib.auth import models as auth_models
from django.db import models

class User(auth_models.User):
    """User that can login/logout + his type."""
    TYPES = (
        (1, 'USER'),
        (2, 'ORGANIZER'),
        # TODO Add Admin if needed
    )

    user_type = models.IntegerField(choices=TYPES)


class Event(models.Model):
    """Event in our DB."""

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey('User')
