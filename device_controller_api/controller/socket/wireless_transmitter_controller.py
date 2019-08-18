from typing import Tuple, List

from device_controller_api.controller.gpio.gpio_controller import GPIOController, PinConfig, PowerLevel


class WirelessTransmitterController:

    def __init__(self, gpio_controller: GPIOController, pin: int):
        self.gpio_controller = gpio_controller
        self.pin = pin
        self.gpio_controller.configure_pin(self.pin, PinConfig.OUTPUT)

    def clear_waves(self):
        self.gpio_controller.clear_waves()

    def send_wave_chain(self, data):
        self.gpio_controller.send_wave_chain(data)

    def create_wave(self, data: List[Tuple[PowerLevel, int]]):
        return self.gpio_controller.create_wave(self.pin, data)
