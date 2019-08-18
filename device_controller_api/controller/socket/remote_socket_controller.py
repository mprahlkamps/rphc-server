from device_controller_api.controller.gpio.gpio_controller import PowerLevel
from device_controller_api.controller.socket.wireless_transmitter_controller import WirelessTransmitterController


class RemoteSocketController:
    def __init__(self, transmitter: WirelessTransmitterController, group: str, device: str):
        self.transmitter = transmitter
        self.group = group
        self.device = device
        self.repeats = 10

        self.t0 = None
        self.t1 = None
        self.tf = None
        self.sync = None
        self.create_waves()

    def enable(self):
        self.send_tri_state(self.get_code_word(self.group, self.device, True))

    def disable(self):
        self.send_tri_state(self.get_code_word(self.group, self.device, False))

    def send_tri_state(self, code_word: str):
        chain = [255, 0]

        for c in code_word:
            if c == '0':
                chain += [self.t0]
            elif c == '1':
                chain += [self.t1]
            elif c == 'F':
                chain += [self.tf]
            else:
                raise RuntimeError("Code error")

        chain += [self.sync, 255, 1, self.repeats, 0]

        self.transmitter.send_wave_chain(chain)

    def create_waves(self):
        self.transmitter.clear_waves()

        wave = [
            (PowerLevel.HIGH, 375),
            (PowerLevel.LOW, 1125),
            (PowerLevel.HIGH, 375),
            (PowerLevel.LOW, 1125),
        ]
        self.t0 = self.transmitter.create_wave(wave)

        wave = [
            (PowerLevel.HIGH, 1125),
            (PowerLevel.LOW, 375),
            (PowerLevel.HIGH, 1125),
            (PowerLevel.LOW, 375),
        ]
        self.t1 = self.transmitter.create_wave(wave)

        wave = [
            (PowerLevel.HIGH, 375),
            (PowerLevel.LOW, 1125),
            (PowerLevel.HIGH, 1125),
            (PowerLevel.LOW, 375),
        ]
        self.tf = self.transmitter.create_wave(wave)

        wave = [
            (PowerLevel.HIGH, 375),
            (PowerLevel.LOW, 9000)
        ]
        self.sync = self.transmitter.create_wave(wave)

    @staticmethod
    def get_code_word(group: str, device: str, status: bool):
        code = ''

        for i in range(5):
            code += 'F' if group[i] == '0' else '0'

        for i in range(5):
            code += 'F' if device[i] == '0' else '0'

        code += '0' if status else 'F'
        code += 'F' if status else '0'

        return code
