from typing import Dict, Any

from device_controller_api.controller.gpio.pigpio_gpio_controller import PigpioGpioController
from device_controller_api.controller.led.abstract_addressable_led import AddressableLedStrip
from device_controller_api.controller.led.abstract_led_strip import LedStrip
from device_controller_api.controller.led.rgb_led_strip import RGBLedStrip
from device_controller_api.controller.led.ws2801_addressable_led_strip import WS2801AddressableLedStrip
from device_controller_api.controller.socket.abstract_remote_socket import RemoteSocket
from device_controller_api.controller.socket.erlo_remote_socket import ErloRemoteSocket
from device_controller_api.models import RemoteSocketModel, GpioControllerModel, AddressableLedStripModel, \
    RGBLedStripModel, WS2801AddressableLedStripModel, ErloRemoteSocketModel


class ControllerManager:
    gpio_controller: Dict[int, Any] = {}
    remote_sockets: Dict[int, RemoteSocket] = {}
    addressable_led_strips: Dict[int, AddressableLedStrip] = {}
    led_strips: Dict[int, LedStrip] = {}

    @staticmethod
    def get_gpio_controller(controller_id: int) -> Any:
        """

        :param controller_id:
        :return:
        """
        if controller_id not in ControllerManager.gpio_controller:
            controller = GpioControllerModel.objects.get(id=controller_id)
            ControllerManager.gpio_controller[controller_id] = PigpioGpioController(controller.hostname,
                                                                                    controller.port)

        return ControllerManager.gpio_controller[controller_id]

    @staticmethod
    def get_addressable_led_strip_controller(led_strip_id: int) -> AddressableLedStrip:
        """

        :param led_strip_id:
        :return:
        """
        if led_strip_id not in ControllerManager.addressable_led_strips:
            led_strip = AddressableLedStripModel.objects.get(id=led_strip_id)
            controller = ControllerManager.get_gpio_controller(led_strip.gpio_controller.id)

            if isinstance(led_strip, WS2801AddressableLedStripModel):
                ControllerManager.addressable_led_strips[led_strip_id] = WS2801AddressableLedStrip(controller,
                                                                                                   led_strip.spi_channel,
                                                                                                   led_strip.spi_frequency,
                                                                                                   led_strip.total_led_count,
                                                                                                   led_strip.usable_led_count)

        return ControllerManager.addressable_led_strips[led_strip_id]

    @staticmethod
    def get_led_strip_controller(led_strip_id: int) -> LedStrip:
        """

        :param led_strip_id:
        :return:
        """
        if led_strip_id not in ControllerManager.led_strips:
            led_strip = AddressableLedStripModel.objects.select_related('gpio_controller').get(id=led_strip_id)
            controller = ControllerManager.get_gpio_controller(led_strip.gpio_controller.id)

            if isinstance(led_strip, RGBLedStripModel):
                ControllerManager.led_strips[led_strip_id] = RGBLedStrip(controller,
                                                                         led_strip.red_pin,
                                                                         led_strip.green_pin,
                                                                         led_strip.red_pin)

        return ControllerManager.led_strips[led_strip_id]

    @staticmethod
    def get_remote_socket_controller(socket_id: int) -> RemoteSocket:
        """

        :param socket_id:
        :return:
        """
        if socket_id not in ControllerManager.remote_sockets:
            remote_socket = RemoteSocketModel.objects.get(id=socket_id)
            controller = ControllerManager.get_gpio_controller(remote_socket.gpio_controller.id)

            if isinstance(remote_socket, ErloRemoteSocketModel):
                ControllerManager.remote_sockets[socket_id] = ErloRemoteSocket(controller,
                                                                               remote_socket.transmitter_pin,
                                                                               remote_socket.group_code,
                                                                               remote_socket.device_code,
                                                                               remote_socket.repeats)

        return ControllerManager.remote_sockets[socket_id]

    @staticmethod
    def clear_gpio_controller():
        ControllerManager.gpio_controller.clear()

    @staticmethod
    def clear_remote_sockets():
        ControllerManager.remote_sockets.clear()

    @staticmethod
    def clear_addressable_led_strips():
        ControllerManager.addressable_led_strips.clear()

    @staticmethod
    def clear_led_strips():
        ControllerManager.led_strips.clear()
