from django.test import TestCase

from device_controller_api.models import PigpioGpioControllerModel


class ControllerTestCase(TestCase):

    def test_create_controller(self):
        try:
            PigpioGpioControllerModel.objects.create(name="controller", hostname="localhost", port=8888)
        except Exception as e:
            self.fail(e)

    def test_controller_str(self):
        controller = PigpioGpioControllerModel.objects.create(name="controller", hostname="localhost", port=8888)
        self.assertEqual(str(controller), "pigpio GPIO Controller (controller)")
