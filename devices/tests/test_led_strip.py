from django.test import TestCase

from devices.models import PiGPIO, RGBLedStrip


class LedStripTestCase(TestCase):

    def setUp(self):
        self.controller = PiGPIO.objects.create(name="controller", hostname="localhost", port=8888)

    def test_create_led_strip(self):
        try:
            RGBLedStrip.objects.create(gpio_controller=self.controller,
                                       name="LED Strip",
                                       red_pin=10,
                                       green_pin=11,
                                       blue_pin=12)
        except Exception as e:
            self.fail(e)

    def test_led_strip_str(self):
        led_strip = RGBLedStrip.objects.create(gpio_controller=self.controller,
                                               name="LED Strip",
                                               red_pin=10,
                                               green_pin=11,
                                               blue_pin=12)

        self.assertEqual(str(led_strip), "RGB LED Strip (LED Strip)")
