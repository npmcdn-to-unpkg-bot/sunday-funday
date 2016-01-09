from django.contrib.auth import models as auth_models
from django.db import models

class User(auth_models.AbstractUser):
    """User that can login/logout + his type."""
    USER = 1
    ORGANISER = 2

    TYPES = (
        (USER, 'USER'),
        (ORGANISER, 'ORGANISER'),
        # TODO Add Admin if needed
    )

    user_type = models.IntegerField(choices=TYPES, default=USER)
    preferences = models.ManyToManyField('Preferences', blank=True) 

    @property
    def name(self):
        return ' '.join([self.first_name.capitalize(),
                         self.last_name.capitalize()])


class Event(models.Model):
    """Event in our DB."""

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey('User')
    preferences = models.ManyToManyField('Preferences', blank=True)

    def __str__(self):
        return self.title

class Preferences(models.Model):
    """ default preferences"""

    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name
