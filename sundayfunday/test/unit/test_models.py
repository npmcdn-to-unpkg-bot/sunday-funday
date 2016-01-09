from django import test
from django import db

from sundayfunday import models

class EventTestCase(test.TestCase):

    def setUp(self):
        self.owner = models.User.objects.create(
                first_name='gigi',
                last_name='becali',
                user_type=models.User.ORGANISER)

    def test_saving(self):
        e = models.Event(title='sometitle',
                         description='abcd',
                         owner=self.owner)
        e.save()


class UserTestCase(test.TestCase):

    def test_type_required(self):
        u = models.User(
                first_name='gigi',
                last_name='becali')
        self.assertRaises(db.IntegrityError, u.save)

    def test_name(self):
        u = models.User(
                first_name='gigi',
                last_name='becali',
                user_type=models.User.USER)
        self.assertEqual(u.name, 'Gigi Becali')

