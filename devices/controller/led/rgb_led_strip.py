from typing import Tuple

from devices.controller.gpio.pigpio_controller import PiGPIOController
from devices.controller.led.led_strip_controller import LedStripController


class RGBLedStripController(LedStripController):

    def __init__(self, gpio_controller: PiGPIOController, red_pin: int, green_pin: int, blue_pin: int):
        self.gpio_controller = gpio_controller
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

    def set_color(self, color: Tuple[int, int, int]):
        pass
