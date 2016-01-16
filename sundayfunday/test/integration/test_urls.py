import httplib

from django import test

from sundayfunday import models
from sundayfunday.forms.register import RegisterUserForm

class TestIndex(test.TestCase):

    def test_index(self):
        c = test.Client()
        response = c.get('/', follow=True)
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

    def tearDown(self):
        self.user.delete()


class TestRegistration(test.TestCase):

    def setUp(self):
        self.c = test.Client()

    def test_succesful_register(self):
        response = self.c.post('/register/', {'username': 'user',
                                 'first_name': 'first_name',
                                 'last_name': 'last_name',
                                 'email': 'email@server.com',
                                 'password1': 'Pass1worder',
                                 'password2': 'Pass1worder'}, follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertEqual(1, models.User.objects.all().count())
        self.assertEqual('user', models.User.objects.all()[0].username)
        models.User.objects.all().delete()

    def test_bad_register(self):
        response = self.c.post('/register/', {'username': 'user',
                                 'first_name': 'first_name',
                                 'last_name': 'last_name',
                                 'email': 'email@server.com',
                                 'password1': 'password',
                                 'password2': 'password'}, follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertEqual(0, models.User.objects.all().count())

    def test_duplicate_user_register(self):
        response = self.c.post('/register/', {'username': 'user',
                                 'first_name': 'first_name',
                                 'last_name': 'last_name',
                                 'email': 'email@server.com',
                                 'password1': 'Pass1worder',
                                 'password2': 'Pass1worder'}, follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertEqual(1, models.User.objects.all().count())
        self.assertEqual('user', models.User.objects.all()[0].username)

        response = self.c.post('/register/', {'username': 'user',
                                 'first_name': 'first_name',
                                 'last_name': 'last_name',
                                 'email': 'email@server.com',
                                 'password1': 'Pass1worder',
                                 'password2': 'Pass1worder'}, follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertEqual(1, models.User.objects.all().count())
        self.assertEqual('user', models.User.objects.all()[0].username)
        models.User.objects.all().delete()

class TestAddEvent(test.TestCase):
    def setUp(self):
        self.c = test.Client()
        self.user = models.User(username='user')
        self.user.set_password('password')
        self.user.save()
        self.c = test.Client()

    def login(self):
        response = self.c.post('/login/', {'username': 'user',
                                           'password': 'password'},
                               follow=True)

    def add_preference(self):
        models.Preference(name='climbing').save()

    def test_succesful_addevent(self):
        self.login();
        self.add_preference();
        response = self.c.post('/addevent/', {'title': 'title',
                                 'description': 'description',
                                 'preference': 'climbing',
                                 }, follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertEqual(1, models.Event.objects.all().count())
        self.assertEqual('title', models.Event.objects.all()[0].title)
        models.Event.objects.all().delete()

    def test_nopreference_addevent(self):
        self.login();
        response = self.c.post('/addevent/', {'title': 'title',
                                 'description': 'description',
                                 'preference': 'climbing',
                                 }, follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertEqual(0, models.Event.objects.all().count())

    def test_nouser_addevent(self):
        response = self.c.post('/addevent/', {'title': 'title',
                                 'description': 'description',
                                 'preference': 'climbing',
                                 }, follow=True)
        self.assertEqual(response.status_code, httplib.OK)
        self.assertEqual(0, models.Event.objects.all().count())
