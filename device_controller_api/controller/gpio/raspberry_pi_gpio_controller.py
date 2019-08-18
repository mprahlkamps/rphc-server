import time
from typing import List, Tuple

import pigpio

from device_controller_api.controller.gpio.gpio_controller import GPIOController, PinConfig, PowerLevel


class RaspberryPiGPIOController(GPIOController):

    def __init__(self, hostname: str, port: int):
        self.controller = pigpio.pi(hostname, port)

    def configure_pin(self, pin: int, config: PinConfig):
        if config == PinConfig.INPUT:
            self.controller.set_mode(pin, pigpio.INPUT)
        elif config == PinConfig.OUTPUT:
            self.controller.set_mode(pin, pigpio.OUTPUT)
        else:
            raise Exception("Unknown Pin configuration")

    def read(self, pin: int) -> PowerLevel:
        return self.controller.read(pin)

    def write(self, pin: int, level: PowerLevel):
        self.controller.write(pin, level)

    def spi_open(self, channel: int, boud: int, flags: int) -> int:
        return self.controller.spi_open(channel, boud, flags)

    def spi_close(self, handle: int) -> None:
        self.controller.spi_close(handle)

    def spi_write(self, handle: int, data: List[int]):
        self.controller.spi_write(handle, data)

    def create_wave(self, pin: int, data: List[Tuple[PowerLevel, int]]):
        wf = []
        for s in data:
            if s[0] == PowerLevel.HIGH:
                wf.append(pigpio.pulse(1 << pin, 0, s[1]))
            elif s[0] == PowerLevel.LOW:
                wf.append(pigpio.pulse(0, 1 << pin, s[1]))

        self.controller.wave_add_generic(wf)
        return self.controller.wave_create()

    def clear_waves(self):
        self.controller.wave_clear()

    def send_wave_chain(self, data):
        self.controller.wave_chain(data)
        while self.controller.wave_tx_busy():
            time.sleep(0.1)
