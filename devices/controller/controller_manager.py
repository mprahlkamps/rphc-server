from typing import Dict, Any

from devices.controller.gpio.pigpio_controller import PiGPIOController
from devices.controller.led.addressable_led_controller import AddressableLedStripController
from devices.controller.led.led_strip_controller import LedStripController
from devices.controller.led.rgb_led_strip import RGBLedStripController
from devices.controller.led.ws2801_addressable_led_strip import WS2801AddressableLedStripController
from devices.controller.socket.erlo_remote_socket_controller import ErloRemoteSocketController
from devices.controller.socket.remote_socket_controller import RemoteSocketController
from devices.controller.socket.sonoff_remote_socket_controller import SonoffRemoteSocketController
from devices.models import RemoteSocket, Controller, AddressableLedStrip, \
    RGBLedStrip, ErloRemoteSocket, SonoffRemoteSocket


class ControllerManager:
    controller: Dict[int, Any] = {}
    remote_socket_controller: Dict[int, RemoteSocketController] = {}
    addressable_led_strip_controller: Dict[int, AddressableLedStripController] = {}
    led_strip_controller: Dict[int, LedStripController] = {}

    @staticmethod
    def get_controller(controller_id: int) -> Any:
        """

        :param controller_id:
        :return:
        """
        if controller_id not in ControllerManager.controller:
            controller = Controller.objects.get(id=controller_id)
            ControllerManager.controller[controller_id] = PiGPIOController(controller.hostname,
                                                                           controller.port)

        return ControllerManager.controller[controller_id]

    @staticmethod
    def get_addressable_led_strip_controller(led_strip_id: int) -> AddressableLedStripController:
        """

        :param led_strip_id:
        :return:
        """
        if led_strip_id not in ControllerManager.addressable_led_strip_controller:
            led_strip = AddressableLedStrip.objects.get(id=led_strip_id)
            controller = ControllerManager.get_controller(led_strip.controller.id)

            if isinstance(led_strip, WS2801AddressableLedStripController):
                ControllerManager.addressable_led_strip_controller[led_strip_id] = WS2801AddressableLedStripController(
                    controller,
                    led_strip.spi_channel,
                    led_strip.spi_frequency,
                    led_strip.total_led_count,
                    led_strip.usable_led_count)

        return ControllerManager.addressable_led_strip_controller[led_strip_id]

    @staticmethod
    def get_led_strip_controller(led_strip_id: int) -> LedStripController:
        """

        :param led_strip_id:
        :return:
        """
        if led_strip_id not in ControllerManager.led_strip_controller:
            led_strip = AddressableLedStrip.objects.get(id=led_strip_id)
            controller = ControllerManager.get_controller(led_strip.controller.id)

            if isinstance(led_strip, RGBLedStrip):
                ControllerManager.led_strip_controller[led_strip_id] = RGBLedStripController(controller,
                                                                                             led_strip.red_pin,
                                                                                             led_strip.green_pin,
                                                                                             led_strip.red_pin)

        return ControllerManager.led_strip_controller[led_strip_id]

    @staticmethod
    def get_remote_socket_controller(socket_id: int) -> RemoteSocketController:
        """

        :param socket_id:
        :return:
        """
        if socket_id not in ControllerManager.remote_socket_controller:
            remote_socket = RemoteSocket.objects.get(id=socket_id)

            if isinstance(remote_socket, ErloRemoteSocket):
                controller = ControllerManager.get_controller(remote_socket.controller.id)
                ControllerManager.remote_socket_controller[socket_id] = ErloRemoteSocketController(controller,
                                                                                                   remote_socket.transmitter_pin,
                                                                                                   remote_socket.group_code,
                                                                                                   remote_socket.device_code,
                                                                                                   remote_socket.repeats)

            if isinstance(remote_socket, SonoffRemoteSocket):
                ControllerManager.remote_socket_controller[socket_id] = SonoffRemoteSocketController(remote_socket.ip,
                                                                                                     remote_socket.port,
                                                                                                     remote_socket.device_id)

        return ControllerManager.remote_socket_controller[socket_id]

    @staticmethod
    def clear_gpio_controller():
        ControllerManager.controller.clear()

    @staticmethod
    def clear_remote_socket_controller():
        ControllerManager.remote_socket_controller.clear()

    @staticmethod
    def clear_addressable_led_strip_controller():
        ControllerManager.addressable_led_strip_controller.clear()

    @staticmethod
    def clear_led_strip_controller():
        ControllerManager.led_strip_controller.clear()
