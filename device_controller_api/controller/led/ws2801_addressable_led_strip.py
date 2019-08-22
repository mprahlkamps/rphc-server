from typing import Tuple

from device_controller_api.controller.gpio.pigpio_gpio_controller import PigpioGpioController
from device_controller_api.controller.led.abstract_addressable_led import AddressableLedStrip


class WS2801AddressableLedStrip(AddressableLedStrip):

    def __init__(self, gpio_controller: PigpioGpioController, spi_channel, spi_frequency, total_led_count,
                 usable_led_count):
        """
        WS2801 Addressable LED controller

        :param gpio_controller:
        :param spi_channel: SPI channel (0-1)
        :param total_led_count: Number of LEDs to use
        """
        self.gpio_controller = gpio_controller
        self.spi_channel = spi_channel
        self.spi_frequency = spi_frequency
        self.total_led_count = total_led_count
        self.usable_led_count = usable_led_count

        self.colors = [0] * (total_led_count * 3)
        self.spi_dev = self.gpio_controller.spi_open(spi_channel, spi_frequency, 3)

    def set_single_color(self, index: int, color: Tuple[int, int, int]):
        self.colors[int(index * 3)] = color[0]
        self.colors[int(index * 3) + 2] = color[1]
        self.colors[int(index * 3) + 1] = color[2]

    def set_color(self, color: Tuple[int, int, int]):
        color = (color[0], color[2], color[1])
        self.colors = list(color * self.usable_led_count) + ([0] * (3 * (self.total_led_count - self.usable_led_count)))

    def show(self):
        self.gpio_controller.spi_write(self.spi_dev, self.colors)

    def close(self):
        self.gpio_controller.spi_close(self.spi_dev)
