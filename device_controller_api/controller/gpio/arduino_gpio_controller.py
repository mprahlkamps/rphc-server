from typing import List, Any

from device_controller_api.controller.gpio.gpio_controller import GPIOController


class ArduinoGPIOController(GPIOController):

    def __init__(self, hostname: str, port: int):
        self.controller = None

    def configure_input_pin(self, pin: int):
        pass

    def configure_output_pin(self, pin: int):
        pass

    def read(self, pin: int):
        pass

    def write(self, pin: int, level: int):
        pass

    def spi_open(self, channel: int, boud: int, flags: int) -> Any:
        pass

    def spi_close(self, handle: Any):
        pass

    def spi_write(self, spi_handle: Any, data: List[int]):
        pass

    def wave_clear(self):
        pass

    def wave_add_generic(self, waves: List[Any]):
        pass

    def wave_create(self) -> Any:
        pass

    def wave_chain(self, data: List[Any]):
        pass

    def wave_tx_busy(self):
        pass
