from django.test import TestCase

from devices.models import PiGPIO


class ControllerTestCase(TestCase):

    def test_create_controller(self):
        try:
            PiGPIO.objects.create(name="controller", hostname="localhost", port=8888)
        except Exception as e:
            self.fail(e)

    def test_controller_str(self):
        controller = PiGPIO.objects.create(name="controller", hostname="localhost", port=8888)
        self.assertEqual(str(controller), "pigpio GPIO Controller (controller)")
