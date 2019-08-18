import json

from django.test import TestCase, Client

from authentication.models import User


class ProgramViewTestCase(TestCase):

    def setUp(self):
        User.objects.create_user("admin@admin.de", "admin")

        self.client = Client()
        response = self.client.post("/api/auth/token/", {"email": "admin@admin.de", "password": "admin"})
        self.access_token = json.loads(response.content.decode('utf-8'))['access']

    def test_list_programs(self):
        resp = self.client.get("/api/programs/", HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.assertEqual(resp.status_code, 200)

    # def test_start_program(self):
    #     resp = self.client.get("/api/programs/start/", HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
    #     self.assertEqual(resp.status_code, 200)
