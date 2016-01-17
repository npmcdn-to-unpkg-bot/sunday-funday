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


    VALID_SUBSCRIBTION = 1
    EXPIRED_SUBSCRIBTION = 2
    FREE_TRIAL = 3

    SUBSCRIBTION_TYPES = (
        (VALID_SUBSCRIBTION, 'VALID'),
        (EXPIRED_SUBSCRIBTION, 'INVALID'),
        (FREE_TRIAL, 'FREE_TRIAL')
    )

    user_type = models.IntegerField(choices=TYPES, default=USER)
    preference = models.ManyToManyField('Preference', blank=True)
    subscribtion_status = models.IntegerField(choices=SUBSCRIBTION_TYPES,
                                              default=FREE_TRIAL)

    @property
    def name(self):
        return ' '.join([self.first_name.capitalize(),
                         self.last_name.capitalize()])

    @property
    def valid_organiser(self):
        if self.user_type != self.ORGANISER:
            return False
        return self.subscribtion_status in [self.VALID_SUBSCRIBTION,
                                            self.FREE_TRIAL]


class Event(models.Model):
    """Event in our DB."""

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey('User')
    preference = models.ManyToManyField('Preference', blank=True)

    def __str__(self):
        return self.title

class AttendEvent(models.Model):
    """ attend event"""

    user = models.ForeignKey('User')
    event = models.ForeignKey('Event')
    data = models.DateTimeField()

    def __str__(self):
        return "%s" % self.id

class Preference(models.Model):
    """ default preferences"""

    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    """ comments for events"""

    comment = models.CharField(max_length=10000)
    date = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s" % self.id

class Grade(models.Model):
    """ event grading"""

    user = models.ForeignKey('User')
    event = models.ForeignKey('Event')

    TYPES = (
        (1, "POOR"),
        (2, "FAIR"),
        (3, "AVERAGE"),
        (4, "GOOD"),
        (5, "EXCELLENT"),
    )
    grade = models.IntegerField(choices=TYPES, default=5)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return "%s" % self.id

class Friend(models.Model):
    """ friending"""

    first_person = models.ForeignKey('User', related_name='person1')
    second_person = models.ForeignKey('User', related_name='person2')
    date = models.DateTimeField()

    def __str__(self):
        return "%s" % self.id
