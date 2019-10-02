from django.test import TestCase

from devices.controller.controller_manager import ControllerManager
from devices.controller.gpio.pigpio_controller import PiGPIOController
from devices.models import PiGPIO


class ControllerManagerTestCase(TestCase):

    def setUp(self):
        ControllerManager.clear_gpio_controller()
        ControllerManager.clear_addressable_led_strip_controller()
        ControllerManager.clear_led_strip_controller()
        ControllerManager.clear_remote_socket_controller()

    def test_get_gpio_controller(self):
        controller = PiGPIO.objects.create(name="pi controller 1",
                                           hostname="localhost",
                                           port=8888)

        self.assertIsInstance(ControllerManager.get_controller(controller.id), PiGPIO)

    # def test_get_addressable_led_controller(self):
    #     controller = PigpioGpioControllerModel.objects.create(name="pi controller 1",
    #                                                           hostname="localhost",
    #                                                           port=8888)
    #
    #     led_strip = WS2801AddressableLedStripModel.objects.create(gpio_controller=controller,
    #                                                               name="test",
    #                                                               total_led_count=160,
    #                                                               usable_led_count=89,
    #                                                               spi_channel=1,
    #                                                               spi_frequency=1000000)
    #
    #     self.assertIsInstance(ControllerManager.get_addressable_led_strip_controller(led_strip.id),
    #                           WS2801AddressableLedStrip)

    # def test_get_remote_socket_controller(self):
    #     controller = PigpioGpioControllerModel.objects.create(name="pi controller 1",
    #                                                           hostname="localhost",
    #                                                           port=8888)
    #     remote_socket = RemoteSocketModel.objects.create(gpio_controller=controller,
    #                                                      name="test",
    #                                                      transmitter_pin=17,
    #                                                      group_code="",
    #                                                      device_code="",
    #                                                      repeats=10)
    #
    #     self.assertIsInstance(ControllerManager.get_remote_socket_controller(remote_socket.id),
    #                           ErloRemoteSocket)
