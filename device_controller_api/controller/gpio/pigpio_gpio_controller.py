import time
from enum import Enum
from typing import List, NamedTuple

import pigpio


class PinMode(Enum):
    INPUT = 0
    OUTPUT = 1


class PowerLevel(Enum):
    LOW = 0
    HIGH = 1


class SpiDevice(NamedTuple):
    handle: int


class Wave(NamedTuple):
    handle: int


class Pulse(NamedTuple):
    level: PowerLevel
    duration: int


class PigpioGpioController:

    def __init__(self, hostname: str, port: int):
        self.controller = pigpio.pi(hostname, port)

    def configure_pin(self, pin: int, mode: PinMode):
        if mode == PinMode.INPUT:
            self.controller.set_mode(pin, pigpio.INPUT)
        elif mode == PinMode.OUTPUT:
            self.controller.set_mode(pin, pigpio.OUTPUT)
        else:
            raise Exception("Unknown pin mode")

    def pin_read(self, pin: int) -> PowerLevel:
        return self.controller.read(pin)

    def pin_write(self, pin: int, level: PowerLevel):
        self.controller.write(pin, level)

    def pin_read_pwm(self, pin: int) -> int:
        pass

    def pin_write_pwm(self, pin: int, pwm: int):
        pass

    def spi_open(self, channel: int, frequency: int, flags: int) -> SpiDevice:
        return SpiDevice(self.controller.spi_open(channel, frequency, flags))

    def spi_close(self, spi_dev: SpiDevice):
        self.controller.spi_close(spi_dev.handle)

    def spi_write(self, spi_dev: SpiDevice, data: List[int]):
        self.controller.spi_write(spi_dev.handle, data)

    def spi_read(self, spi_dev: SpiDevice, count: int):
        return self.controller.spi_read(spi_dev.handle, count)

    def create_wave(self, pin: int, pulses: List[Pulse]):
        wave = []
        for pulse in pulses:
            if pulse.level == PowerLevel.HIGH:
                wave.append(pigpio.pulse(1 << pin, 0, pulse.duration))
            elif pulse.level == PowerLevel.LOW:
                wave.append(pigpio.pulse(0, 1 << pin, pulse.duration))

        self.controller.wave_add_generic(wave)
        return Wave(self.controller.wave_create())

    def clear_waves(self):
        self.controller.wave_clear()

    def send_wave_chain(self, data):
        self.controller.wave_chain(data)
        while self.controller.wave_tx_busy():
            time.sleep(0.1)
