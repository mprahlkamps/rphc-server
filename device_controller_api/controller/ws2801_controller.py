class WS2801Controller:

    def __init__(self, pi_control, device, led_count):
        """
        WS2801 Addressable LED controller

        :param pi_control: pigpio instance
        :param device: SPI device (0-1)
        :param led_count: Number of LEDs to use
        """
        self.pi_control = pi_control
        self.device = device
        self.led_count = led_count

        self.colors = [0] * (led_count * 3)
        self.spi_handle = self.pi_control.spi_open(0, 1000000, 3)

    def set_color(self, index: int, r: int, g: int, b: int):
        self.colors[int(index * 3)] = r
        self.colors[int(index * 3) + 2] = g
        self.colors[int(index * 3) + 1] = b

    def show(self):
        self.pi_control.spi_write(self.spi_handle, self.colors)

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
        self.pi_control.spi_write(self.spi_handle, clear_colors)

    def close(self):
        self.pi_control.spi_close(self.spi_handle)

    def start_program(self):
        pass
