from typing import Dict

import pigpio

from device_controller_api.controller.remote_socket_controller import RemoteSocketController
from device_controller_api.controller.transmitter_controller import TransmitterController
from device_controller_api.controller.ws2801_controller import WS2801Controller
from device_controller_api.models import Controller, AddressableLEDStrip, Transmitter, RemoteSocket


class ControllerManager:
    pi_controller: Dict[int, pigpio.pi] = {}
    transmitter_controller: Dict[int, TransmitterController] = {}
    remote_socket_controller: Dict[int, RemoteSocketController] = {}
    addressable_led_controller: Dict[int, WS2801Controller] = {}

    def __init__(self):
        pass

    @staticmethod
    def get_pi_controller(pi_id: int) -> pigpio.pi:
        """

        :param pi_id:
        :return:
        """
        if pi_id not in ControllerManager.pi_controller:
            controller = Controller.objects.get(id=pi_id)
            ControllerManager.pi_controller[pi_id] = pigpio.pi(controller.hostname, controller.port)

        return ControllerManager.pi_controller[pi_id]

    @staticmethod
    def get_addressable_led_strip_controller(led_strip_id: int) -> WS2801Controller:
        """

        :param led_strip_id:
        :return:
        """
        if led_strip_id not in ControllerManager.addressable_led_controller:
            led_strip = AddressableLEDStrip.objects.select_related('controller').get(id=led_strip_id)
            controller = ControllerManager.get_pi_controller(led_strip.controller.id)
            ControllerManager.addressable_led_controller[led_strip_id] = WS2801Controller(controller,
                                                                                          led_strip.spi_device,
                                                                                          led_strip.led_count)

        return ControllerManager.addressable_led_controller[led_strip_id]

    @staticmethod
    def get_transmitter_controller(transmitter_id: int) -> TransmitterController:
        """

        :param transmitter_id:
        :return:
        """
        if transmitter_id not in ControllerManager.transmitter_controller:
            transmitter = Transmitter.objects.select_related('controller').get(id=transmitter_id)
            controller = ControllerManager.get_pi_controller(transmitter.controller.id)
            ControllerManager.transmitter_controller[transmitter_id] = TransmitterController(controller,
                                                                                             transmitter.pin,
                                                                                             transmitter.retries)

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
