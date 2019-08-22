from django.test import TestCase

from device_controller_api.models import PigpioGpioControllerModel, RGBLedStripModel


class LedStripTestCase(TestCase):

    def setUp(self):
        self.controller = PigpioGpioControllerModel.objects.create(name="controller", hostname="localhost", port=8888)

    def test_create_led_strip(self):
        try:
            RGBLedStripModel.objects.create(gpio_controller=self.controller,
                                            name="LED Strip",
                                            red_pin=10,
                                            green_pin=11,
                                            blue_pin=12)
        except Exception as e:
            self.fail(e)

    def test_led_strip_str(self):
        led_strip = RGBLedStripModel.objects.create(gpio_controller=self.controller,
                                                    name="LED Strip",
                                                    red_pin=10,
                                                    green_pin=11,
                                                    blue_pin=12)

        self.assertEqual(str(led_strip), "RGB LED Strip (LED Strip)")
