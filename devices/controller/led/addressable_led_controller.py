from abc import ABC, abstractmethod
from typing import Tuple


class AddressableLedStripController(ABC):

    @abstractmethod
    def set_color(self, color: Tuple[int, int, int]):
        pass

    @abstractmethod
    def set_single_color(self, index: int, color: Tuple[int, int, int]):
        pass

    @abstractmethod
    def show(self):
        pass
