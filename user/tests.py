from django.test import TestCase
from user.models import User


class UserManagerTestCase(TestCase):
    email = "tester@mozillaz.org"
    username = "tester"

    def test_create_user(self):
        user = User.objects.create_user(username=self.username, email=self.email, password="test")
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.username, self.username)
        self.assertTrue(user.has_usable_password())

    def test_empty_username(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='')

    def test_empty_email(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username=self.username)
