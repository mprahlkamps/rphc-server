from django.test import TestCase

from device_controller_api.controller.controller_manager import ControllerManager
from device_controller_api.controller.gpio.fake_gpio_controller import FakeGPIOController
from device_controller_api.models import RemoteGPIOController


class ControllerManagerTestCase(TestCase):

    def test_get_gpio_controller(self):
        controller = RemoteGPIOController.objects.create(name="pi controller 1",
                                                         hostname="localhost",
                                                         port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)
        controller.save()

        self.assertIsInstance(ControllerManager.get_gpio_controller(controller.id), FakeGPIOController)
