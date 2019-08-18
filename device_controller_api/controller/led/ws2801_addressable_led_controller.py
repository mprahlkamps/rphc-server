from typing import Tuple

from device_controller_api.controller.gpio.gpio_controller import GPIOController
from device_controller_api.controller.led.addressable_led_controller import AddressableLEDController


class WS2801AddressableLEDController(AddressableLEDController):

    def __init__(self, gpio_controller: GPIOController, spi_channel, led_count, usable_led_count):
        """
        WS2801 Addressable LED controller

        :param gpio_controller:
        :param spi_channel: SPI channel (0-1)
        :param led_count: Number of LEDs to use
        """
        self.gpio_controller = gpio_controller
        self.spi_channel = spi_channel
        self.led_count = led_count
        self.usable_led_count = usable_led_count

        self.colors = [0] * (led_count * 3)
        self.spi_handle = self.gpio_controller.spi_open(self.spi_channel, 1000000, 3)

    def set_single_color(self, index: int, color: Tuple[int, int, int]):
        self.colors[int(index * 3)] = color[0]
        self.colors[int(index * 3) + 2] = color[1]
        self.colors[int(index * 3) + 1] = color[2]

    def set_color(self, color: Tuple[int, int, int]):
        color = (color[0], color[2], color[1])
        self.colors = list(color * self.led_count) + ([0] * (3 * (self.led_count - self.usable_led_count)))

    def show(self):
        self.gpio_controller.spi_write(self.spi_handle, self.colors)

    def close(self):
        self.gpio_controller.spi_close(self.spi_handle)
