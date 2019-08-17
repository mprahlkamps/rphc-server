from typing import List, Any

import pigpio

from device_controller_api.controller.gpio.gpio_controller import GPIOController


class RaspberryPiGPIOController(GPIOController):

    def __init__(self, hostname: str, port: int):
        self.controller = pigpio.pi(hostname, port)

    def configure_input_pin(self, pin: int):
        self.controller.set_mode(pin, pigpio.INPUT)

    def configure_output_pin(self, pin: int):
        self.controller.set_mode(pin, pigpio.OUTPUT)

    def read(self, pin: int) -> int:
        return self.controller.read(pin)

    def write(self, pin: int, level: int):
        self.controller.write(pin, level)

    def spi_open(self, channel: int, boud: int, flags: int) -> int:
        return self.controller.spi_open(channel, boud, flags)

    def spi_close(self, handle: int) -> None:
        self.controller.spi_close(handle)

    def spi_write(self, handle: int, data: List[int]):
        self.controller.spi_write(handle, data)

    def wave_clear(self):
        self.controller.wave_clear()

    def wave_add_generic(self, waves: List[Any]):
        self.controller.wave_add_generic(waves)

    def wave_create(self) -> Any:
        return self.controller.wave_create()

    def wave_chain(self, data: List[Any]):
        self.controller.wave_chain(data)

    def wave_tx_busy(self):
        self.controller.wave_tx_busy()
