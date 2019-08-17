from device_controller_api.controller.gpio.gpio_controller import GPIOController


class WS2801Controller:

    def __init__(self, gpio_controller: GPIOController, spi_channel, led_count):
        """
        WS2801 Addressable LED controller

        :param gpio_controller:
        :param spi_channel: SPI channel (0-1)
        :param led_count: Number of LEDs to use
        """
        self.gpio_controller = gpio_controller
        self.spi_channel = spi_channel
        self.led_count = led_count

        self.colors = [0] * (led_count * 3)
        self.spi_handle = self.gpio_controller.spi_open(self.spi_channel, 1000000, 3)

    def set_color(self, index: int, r: int, g: int, b: int):
        self.colors[int(index * 3)] = r
        self.colors[int(index * 3) + 2] = g
        self.colors[int(index * 3) + 1] = b

    def show(self):
        self.gpio_controller.spi_write(self.spi_handle, self.colors)

    def set_color_all(self, r: int, g: int, b: int):
        self.colors = [r, b, g] * self.led_count

    def set_color_until(self, n: int, r: int, g: int, b: int):
        """

        :param n:
        :param r:
        :param g:
        :param b:
        :return:
        """
        if n > self.led_count:
            raise RuntimeError("n must be <= led_count")

        self.colors = [r, b, g] * n

    def clear(self, led_count: int):
        """
        Clears the LED strip (no show call needed!)

        :param led_count: How many LEDs to clear. Can be greater than led_count
        :return: None
        """
        clear_colors = [0, 0, 0] * led_count
        self.gpio_controller.spi_write(self.spi_handle, clear_colors)

    def close(self):
        self.gpio_controller.spi_close(self.spi_handle)
