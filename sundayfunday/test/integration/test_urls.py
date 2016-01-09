import httplib

from django import test

from sundayfunday import models

class TestIndex(test.TestCase):

    def test_index(self):
        c = test.Client()
        response = c.get('/')
        self.assertEqual(response.status_code, httplib.OK)


class TestLoginLogout(test.TestCase):

    def setUp(self):
        self.user = models.User(username='user')
        self.user.set_password('password')
        self.user.save()
        self.c = test.Client()

    def test_login(self):
        response = self.c.post('/login/', {'username': 'user',
                                           'password': 'password'},
                               follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertTrue(response.context['user'].is_authenticated())

    def test_bad_user(self):
        response = self.c.post('/login/', {'username': 'nouser',
                                           'password': 'password'})
        self.assertEqual(response.status_code, httplib.UNAUTHORIZED)
        self.assertFalse(response.context['user'].is_authenticated())

    def test_bad_pass(self):
        response = self.c.post('/login/', {'username': 'user',
                                           'password': 'badpass'})
        self.assertEqual(response.status_code, httplib.UNAUTHORIZED)
        self.assertFalse(response.context['user'].is_authenticated())

    def test_logout(self):
        response = self.c.post('/login/', {'username': 'user',
                                           'password': 'password'},
                               follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertTrue(response.context['user'].is_authenticated())
        response = self.c.get('/logout/', follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertFalse(response.context['user'].is_authenticated())





