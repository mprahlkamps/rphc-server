from django.test import TestCase

from device_controller_api.controller.controller_manager import ControllerManager
from device_controller_api.controller.gpio.fake_gpio_controller import FakeGPIOController
from device_controller_api.controller.led.ws2801_addressable_led_controller import WS2801AddressableLEDController
from device_controller_api.controller.socket.remote_socket_controller import RemoteSocketController
from device_controller_api.controller.socket.wireless_transmitter_controller import WirelessTransmitterController
from device_controller_api.models import RemoteGPIOController, AddressableLEDStrip, RemoteSocket, \
    WirelessTransmitter


class ControllerManagerTestCase(TestCase):

    def setUp(self):
        ControllerManager.clear_gpio_controller()
        ControllerManager.clear_addressable_led_controller()
        ControllerManager.clear_remote_socket_controller()
        ControllerManager.clear_transmitter_controller()

    def test_get_gpio_controller(self):
        controller = RemoteGPIOController.objects.create(name="pi controller 1",
                                                         hostname="localhost",
                                                         port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)

        self.assertIsInstance(ControllerManager.get_gpio_controller(controller.id), FakeGPIOController)

    def test_get_unknown_gpio_controller(self):
        controller = RemoteGPIOController.objects.create(name="pi controller 1",
                                                         hostname="localhost",
                                                         port=8888,
                                                         type="XX")

        with self.assertRaises(Exception):
            ControllerManager.get_gpio_controller(controller.id)

    def test_get_addressable_led_controller(self):
        controller = RemoteGPIOController.objects.create(name="pi controller 1",
                                                         hostname="localhost",
                                                         port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)

        led_strip = AddressableLEDStrip.objects.create(controller=controller, name="test", led_count=200,
                                                       usable_led_count=89, spi_device=1,
                                                       type=AddressableLEDStrip.WS2801)

        self.assertIsInstance(ControllerManager.get_addressable_led_strip_controller(led_strip.id),
                              WS2801AddressableLEDController)

    def test_get_unknown_addressable_led_controller(self):
        controller = RemoteGPIOController.objects.create(name="pi controller 1",
                                                         hostname="localhost",
                                                         port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)

        led_strip = AddressableLEDStrip.objects.create(controller=controller, name="test", led_count=200,
                                                       usable_led_count=89, spi_device=1,
                                                       type="XX")

        with self.assertRaises(Exception):
            ControllerManager.get_addressable_led_strip_controller(led_strip.id)

    def test_get_remote_socket_controller(self):
        controller = RemoteGPIOController.objects.create(name="pi controller 1",
                                                         hostname="localhost",
                                                         port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)

        transmitter = WirelessTransmitter.objects.create(controller=controller, name="test", pin=1)
        remote_socket = RemoteSocket.objects.create(transmitter=transmitter, name="test", group="", device="",
                                                    repeats=10)

        self.assertIsInstance(ControllerManager.get_remote_socket_controller(remote_socket.id),
                              RemoteSocketController)

    def test_get_transmitter_controller(self):
        controller = RemoteGPIOController.objects.create(name="pi controller 1",
                                                         hostname="localhost",
                                                         port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)

        transmitter = WirelessTransmitter.objects.create(controller=controller, name="test", pin=1)

        self.assertIsInstance(ControllerManager.get_transmitter_controller(transmitter.id),
                              WirelessTransmitterController)
