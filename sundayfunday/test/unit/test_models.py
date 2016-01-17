from django import test

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

    def test_type_is_user(self):
        u = models.User(
                first_name='gigi',
                last_name='becali')
        u.save()
        self.assertEqual(u.user_type, models.User.USER)

    def test_name(self):
        u = models.User(
                first_name='gigi',
                last_name='becali',
                user_type=models.User.USER)
        self.assertEqual(u.name, 'Gigi Becali')

    def test_valid_user(self):
        u_default_ft = models.User(user_type=models.User.ORGANISER,
                                   username='username1')
        u_default_ft.save()
        self.assertTrue(u_default_ft.valid_organiser)
        u_ft = models.User(user_type=models.User.ORGANISER,
                           subscribtion_status=models.User.FREE_TRIAL,
                           username='username2')
        u_ft.save()
        self.assertTrue(u_ft.valid_organiser)
        u_exp = models.User(user_type=models.User.ORGANISER,
                            subscribtion_status=models.User.EXPIRED_SUBSCRIBTION,
                            username='username3')
        u_exp.save()
        self.assertFalse(u_exp.valid_organiser)
        u_valid = models.User(user_type=models.User.ORGANISER,
                              subscribtion_status=models.User.VALID_SUBSCRIBTION,
                              username='username4')
        u_valid.save()
        self.assertTrue(u_valid.valid_organiser)
        u_regular = models.User(user_type=models.User.USER,
                                username='username5')
        u_regular.save()
        self.assertFalse(u_regular.valid_organiser)

