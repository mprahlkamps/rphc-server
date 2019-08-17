from abc import ABC, abstractmethod
from typing import Any, List


class GPIOController(ABC):

    @abstractmethod
    def configure_input_pin(self, pin: int):
        """

        :param pin:
        :return:
        """
        pass

    @abstractmethod
    def configure_output_pin(self, pin: int):
        """

        :param pin:
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
    def wave_clear(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def wave_add_generic(self, waves: List[Any]) -> Any:
        """

        :param waves:
        :return:
        """
        pass

    @abstractmethod
    def wave_create(self) -> Any:
        """

        :return:
        """
        pass

    @abstractmethod
    def wave_chain(self, data: List[Any]):
        """

        :param data:
        :return:
        """
        pass

    @abstractmethod
    def wave_tx_busy(self):
        """

        :return:
        """
        pass
