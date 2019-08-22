from typing import Tuple

from device_controller_api.controller.gpio.pigpio_gpio_controller import PigpioGpioController
from device_controller_api.controller.led.abstract_led_strip import LedStrip


class RGBLedStrip(LedStrip):

    def __init__(self, gpio_controller: PigpioGpioController, red_pin: int, green_pin: int, blue_pin: int):
        self.gpio_controller = gpio_controller
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

    def set_color(self, color: Tuple[int, int, int]):
        pass
