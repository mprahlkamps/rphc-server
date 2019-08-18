from django.test import TestCase

from device_controller_api.models import RemoteGPIOController


class ControllerTestCase(TestCase):

    def test_create_controller(self):
        try:
            RemoteGPIOController.objects.create(name="controller", hostname="localhost", port=8888,
                                                type=RemoteGPIOController.FAKE_CONTROLLER)
        except Exception as e:
            self.fail(e)

    def test_controller_str(self):
        controller = RemoteGPIOController.objects.create(name="controller", hostname="localhost", port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)
        self.assertEqual(str(controller), "GPIO Controller (controller)")

        controller = RemoteGPIOController.objects.create(name="test", hostname="localhost", port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)
        self.assertEqual(str(controller), "GPIO Controller (test)")
