from abc import ABC, abstractmethod
from typing import Tuple


class LEDController(ABC):

    @abstractmethod
    def set_color(self, color: Tuple[int, int, int]):
        pass
