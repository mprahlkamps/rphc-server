from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, List, Tuple


class PinConfig(Enum):
    INPUT = 0
    OUTPUT = 1


class PowerLevel(Enum):
    LOW = 0
    HIGH = 1


class GPIOController(ABC):

    @abstractmethod
    def configure_pin(self, pin: int, config: PinConfig):
        """

        :param pin:
        :param config:
        :return:
        """
        pass

    @abstractmethod
    def read(self, pin: int):
        """

        :param pin:
        :return:
        """
        pass

    @abstractmethod
    def write(self, pin: int, level: int):
        """

        :param pin:
        :param level:
        :return:
        """
        pass

    @abstractmethod
    def spi_open(self, channel: int, boud: int, flags: int) -> Any:
        """

        :param channel:
        :param boud:
        :param flags:
        :return:
        """
        pass

    @abstractmethod
    def spi_close(self, handle: Any):
        """

        :param handle:
        :return:
        """
        pass

    @abstractmethod
    def spi_write(self, spi_handle: Any, data: List[int]):
        """

        :param spi_handle:
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def create_wave(self, pin: int, data: List[Tuple[PowerLevel, int]]):
        """
        data = [
            (HIGH/LOW, time),
            (HIGH/LOW, time),
            (HIGH/LOW, time),
            ...
        ]
        :param pin:
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def clear_waves(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def send_wave_chain(self, data):
        """

        :param data:
        :return:
        """
        pass
