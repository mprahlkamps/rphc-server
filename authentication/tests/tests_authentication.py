import json

from django.test import TestCase, Client

from authentication.models import User


class AuthenticationTest(TestCase):

    def setUp(self):
        user = User.objects.create_user("admin@admin.de", "admin")
        user.save()
        self.client = Client()

    def tearDown(self):
        pass

    def test_authenticate(self):
        response = self.client.post('/api/auth/token/',
                                    content_type="application/json",
                                    data={"email": "admin@admin.de", "password": "admin"})

        self.assertEqual(response.status_code, 200)

    def test_authenticate_false(self):
        response = self.client.post('/api/auth/token/',
                                    content_type="application/json",
                                    data={"email": "admin@admin.de", "password": "wrong_password"})

        self.assertEqual(response.status_code, 401)

    def test_authenticate_no_data(self):
        response = self.client.post('/api/auth/token/',
                                    content_type="application/json")

        self.assertEqual(response.status_code, 400)

    def test_refresh(self):
        response = self.client.post('/api/auth/token/',
                                    content_type="application/json",
                                    data={"email": "admin@admin.de", "password": "admin"})

        self.assertEqual(response.status_code, 200)
        refresh_token = json.loads(response.content.decode('utf-8'))['refresh']

        response = self.client.post('/api/auth/token/refresh/',
                                    content_type="application/json",
                                    data={"refresh": refresh_token})

        self.assertEqual(response.status_code, 200)
