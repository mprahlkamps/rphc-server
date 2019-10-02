import json

from django.test import TestCase, Client

from authentication.models import User
from devices.models import PiGPIO, WS2801AddressableLedStrip


class AddressableLedViewTestCase(TestCase):

    def setUp(self):
        User.objects.create_user("admin@admin.de", "admin")
        controller = PiGPIO.objects.create(name="controller", hostname="localhost", port=8888)

        WS2801AddressableLedStrip.objects.create(gpio_controller=controller, name="led",
                                                 total_led_count=160,
                                                 usable_led_count=89,
                                                 spi_channel=0,
                                                 spi_frequency=1000000)

        self.client = Client()
        response = self.client.post("/api/auth/token/", {"email": "admin@admin.de", "password": "admin"})
        self.access_token = json.loads(response.content.decode('utf-8'))['access']

    # def test_set_led_color(self):
    #     resp = self.client.post("/api/devices/addressable-led-strip/1/set-color/", {"r": 0, "g": 0, "b": 0},
    #                             HTTP_AUTHORIZATION='Bearer ' + self.access_token)
    #
    #     self.assertEqual(resp.status_code, 200)
