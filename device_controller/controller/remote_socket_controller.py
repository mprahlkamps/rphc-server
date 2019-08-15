from device_controller.controller.transmitter_controller import TransmitterController


class RemoteSocketController:
    def __init__(self, transmitter: TransmitterController, group: str, device: str):
        self.transmitter = transmitter
        self.group = group
        self.device = device

    def enable(self):
        self.transmitter.enable(self.group, self.device)

    def disable(self):
        self.transmitter.disable(self.group, self.device)
