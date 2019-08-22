from abc import ABC, abstractmethod


class RemoteSocket(ABC):

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass
