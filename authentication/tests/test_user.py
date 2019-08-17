from django.test import TestCase

from authentication.models import User


class AuthenticationTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_no_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="admin")

    def test_user_to_str(self):
        user = User.objects.create_user(email="admin@admin.de", password="admin")
        self.assertEqual(str(user), "admin@admin.de")

    def test_user_full_name(self):
        user = User.objects.create_user(email="admin@admin.de", password="admin")
        self.assertEqual(user.get_full_name(), "admin@admin.de")

    def test_user_short_name(self):
        user = User.objects.create_user(email="admin@admin.de", password="admin")
        self.assertEqual(user.get_short_name(), "admin@admin.de")
