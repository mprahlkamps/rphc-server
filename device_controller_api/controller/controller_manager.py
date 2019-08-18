from typing import Dict

from device_controller_api.controller.gpio.arduino_gpio_controller import ArduinoGPIOController
from device_controller_api.controller.gpio.fake_gpio_controller import FakeGPIOController
from device_controller_api.controller.gpio.gpio_controller import GPIOController
from device_controller_api.controller.gpio.raspberry_pi_gpio_controller import RaspberryPiGPIOController
from device_controller_api.controller.led.ws2801_addressable_led_controller import WS2801AddressableLEDController
from device_controller_api.controller.socket.remote_socket_controller import RemoteSocketController
from device_controller_api.controller.socket.wireless_transmitter_controller import WirelessTransmitterController
from device_controller_api.models import RemoteGPIOController, AddressableLEDStrip, WirelessTransmitter, RemoteSocket


class ControllerManager:
    gpio_controller: Dict[int, GPIOController] = {}
    transmitter_controller: Dict[int, WirelessTransmitterController] = {}
    remote_socket_controller: Dict[int, RemoteSocketController] = {}
    addressable_led_controller: Dict[int, WS2801AddressableLEDController] = {}

    @staticmethod
    def get_gpio_controller(controller_id: int) -> GPIOController:
        """

        :param controller_id:
        :return:
        """
        if controller_id not in ControllerManager.gpio_controller:
            controller = RemoteGPIOController.objects.get(id=controller_id)

            if controller.type == RemoteGPIOController.RASPBERRY_PI_CONTROLLER:
                ControllerManager.gpio_controller[controller_id] = RaspberryPiGPIOController(controller.hostname,
                                                                                             controller.port)
            elif controller.type == RemoteGPIOController.ARDUINO_CONTROLLER:
                ControllerManager.gpio_controller[controller_id] = ArduinoGPIOController(controller.hostname,
                                                                                         controller.port)
            elif controller.type == RemoteGPIOController.FAKE_CONTROLLER:
                ControllerManager.gpio_controller[controller_id] = FakeGPIOController()
            else:
                raise Exception("Unknown controller type")

        return ControllerManager.gpio_controller[controller_id]

    @staticmethod
    def get_addressable_led_strip_controller(led_strip_id: int) -> WS2801AddressableLEDController:
        """

        :param led_strip_id:
        :return:
        """
        if led_strip_id not in ControllerManager.addressable_led_controller:
            led_strip = AddressableLEDStrip.objects.select_related('controller').get(id=led_strip_id)
            controller = ControllerManager.get_gpio_controller(led_strip.controller.id)

            if led_strip.type == AddressableLEDStrip.WS2801:
                ControllerManager.addressable_led_controller[led_strip_id] = WS2801AddressableLEDController(controller,
                                                                                                            led_strip.spi_device,
                                                                                                            led_strip.led_count,
                                                                                                            led_strip.usable_led_count)
            else:
                raise Exception("Unknown addressable led type")

        return ControllerManager.addressable_led_controller[led_strip_id]

    @staticmethod
    def get_transmitter_controller(transmitter_id: int) -> WirelessTransmitterController:
        """

        :param transmitter_id:
        :return:
        """
        if transmitter_id not in ControllerManager.transmitter_controller:
            transmitter = WirelessTransmitter.objects.select_related('controller').get(id=transmitter_id)
            controller = ControllerManager.get_gpio_controller(transmitter.controller.id)
            ControllerManager.transmitter_controller[transmitter_id] = WirelessTransmitterController(controller,
                                                                                                     transmitter.pin)

        return ControllerManager.transmitter_controller[transmitter_id]

    @staticmethod
    def get_remote_socket_controller(socket_id: int) -> RemoteSocketController:
        """

        :param socket_id:
        :return:
        """
        if socket_id not in ControllerManager.remote_socket_controller:
            remote_socket = RemoteSocket.objects.select_related('transmitter').get(id=socket_id)
            transmitter = ControllerManager.get_transmitter_controller(remote_socket.transmitter.id)
            ControllerManager.remote_socket_controller[socket_id] = RemoteSocketController(transmitter,
                                                                                           remote_socket.group,
                                                                                           remote_socket.device)

        return ControllerManager.remote_socket_controller[socket_id]
