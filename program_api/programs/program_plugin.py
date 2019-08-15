from abc import ABC, abstractmethod


class ProgramPlugin(ABC):
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_stop(self):
        pass

    @abstractmethod
    def set_variables(self, variables):
        pass

    @abstractmethod
    def update(self, seconds, dt):
        pass
