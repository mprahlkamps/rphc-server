from devices.controller.gpio.pigpio_controller import PiGPIOController, Pulse, PowerLevel, \
    PinMode
from devices.controller.socket.remote_socket_controller import RemoteSocketController


class ErloRemoteSocketController(RemoteSocketController):

    def __init__(self, gpio_controller: PiGPIOController, transmitter_pin: int, group_code: str, device_code: str,
                 repeats: int):
        self.gpio_controller = gpio_controller
        self.transmitter_pin = transmitter_pin
        self.group_code = group_code
        self.device_code = device_code
        self.repeats = repeats

        self.gpio_controller.configure_pin(self.transmitter_pin, PinMode.OUTPUT)

        self.t0 = None
        self.t1 = None
        self.tf = None
        self.sync = None
        self.create_waves()

    def enable(self):
        self.send_tri_state(self.get_code_word(self.group_code, self.device_code, True))

    def disable(self):
        self.send_tri_state(self.get_code_word(self.group_code, self.device_code, False))

    def status(self):
        raise NotImplementedError("Status not available for Erlo Remote Sockets")

    def send_tri_state(self, code_word: str):
        chain = [255, 0]

        for c in code_word:
            if c == '0':
                chain += [self.t0.handle]
            elif c == '1':
                chain += [self.t1.handle]
            elif c == 'F':
                chain += [self.tf.handle]
            else:
                raise RuntimeError("Code error")

        chain += [self.sync.handle, 255, 1, self.repeats, 0]

        self.gpio_controller.send_wave_chain(chain)

    def create_waves(self):
        self.gpio_controller.clear_waves()

        wave = [
            Pulse(level=PowerLevel.HIGH, duration=375),
            Pulse(PowerLevel.LOW, 1125),
            Pulse(PowerLevel.HIGH, 375),
            Pulse(PowerLevel.LOW, 1125),
        ]
        self.t0 = self.gpio_controller.create_wave(self.transmitter_pin, wave)

        wave = [
            Pulse(PowerLevel.HIGH, 1125),
            Pulse(PowerLevel.LOW, 375),
            Pulse(PowerLevel.HIGH, 1125),
            Pulse(PowerLevel.LOW, 375),
        ]
        self.t1 = self.gpio_controller.create_wave(self.transmitter_pin, wave)

        wave = [
            Pulse(PowerLevel.HIGH, 375),
            Pulse(PowerLevel.LOW, 1125),
            Pulse(PowerLevel.HIGH, 1125),
            Pulse(PowerLevel.LOW, 375),
        ]
        self.tf = self.gpio_controller.create_wave(self.transmitter_pin, wave)

        wave = [
            Pulse(PowerLevel.HIGH, 375),
            Pulse(PowerLevel.LOW, 9000)
        ]
        self.sync = self.gpio_controller.create_wave(self.transmitter_pin, wave)

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
