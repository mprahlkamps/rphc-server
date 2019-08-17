from django.test import TestCase

from device_controller_api.models import LEDStrip, RemoteGPIOController


class LEDStripTestCase(TestCase):

    def setUp(self):
        self.controller = RemoteGPIOController.objects.create(name="controller", hostname="localhost", port=8888,
                                                              controller_type=RemoteGPIOController.FAKE_CONTROLLER)
        self.controller.save()

    def test_create_led_strip(self):
        try:
            led_strip = LEDStrip.objects.create(controller=self.controller,
                                                name="LED Strip",
                                                red_pin=10,
                                                green_pin=11,
                                                blue_pin=12)
            led_strip.save()
        except Exception as e:
            self.fail(e)

    def test_led_strip_str(self):
        led_strip = LEDStrip.objects.create(controller=self.controller,
                                            name="LED Strip",
                                            red_pin=10,
                                            green_pin=11,
                                            blue_pin=12)

        self.assertEqual(str(led_strip), "LED Strip (10,11,12)")

        led_strip = LEDStrip.objects.create(controller=self.controller,
                                            name="LED Strip",
                                            red_pin=20,
                                            green_pin=21,
                                            blue_pin=22)

        self.assertEqual(str(led_strip), "LED Strip (20,21,22)")
