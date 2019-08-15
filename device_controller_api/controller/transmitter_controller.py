import time

import pigpio


class TransmitterController:

    def __init__(self, pi_control: pigpio.pi, pin: int, repeats: int):
        self.pi_control = pi_control
        self.pin = pin
        self.repeats = repeats

        self.t0 = None
        self.t1 = None
        self.tf = None
        self.sync = None
        self.create_waves()

        self.pi_control.set_mode(self.pin, pigpio.OUTPUT)

    def enable(self, group: str, device: str):
        self.send_tri_state(self.get_code_word(group, device, True))

    def disable(self, group: str, device: str):
        self.send_tri_state(self.get_code_word(group, device, False))

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

        self.pi_control.wave_chain(chain)

        while self.pi_control.wave_tx_busy():
            time.sleep(0.1)

    def create_waves(self):
        self.pi_control.wave_clear()

        wf = [
            pigpio.pulse(1 << self.pin, 0, 375),
            pigpio.pulse(0, 1 << self.pin, 1125),
            pigpio.pulse(1 << self.pin, 0, 375),
            pigpio.pulse(0, 1 << self.pin, 1125)
        ]
        self.pi_control.wave_add_generic(wf)
        self.t0 = self.pi_control.wave_create()

        wf = [
            pigpio.pulse(1 << self.pin, 0, 1125),
            pigpio.pulse(0, 1 << self.pin, 375),
            pigpio.pulse(1 << self.pin, 0, 1125),
            pigpio.pulse(0, 1 << self.pin, 375),
        ]
        self.pi_control.wave_add_generic(wf)
        self.t1 = self.pi_control.wave_create()

        wf = [
            pigpio.pulse(1 << self.pin, 0, 375),
            pigpio.pulse(0, 1 << self.pin, 1125),
            pigpio.pulse(1 << self.pin, 0, 1125),
            pigpio.pulse(0, 1 << self.pin, 375),
        ]
        self.pi_control.wave_add_generic(wf)
        self.tf = self.pi_control.wave_create()

        wf = [
            pigpio.pulse(1 << self.pin, 0, 375),
            pigpio.pulse(0, 1 << self.pin, 9000)
        ]
        self.pi_control.wave_add_generic(wf)
        self.sync = self.pi_control.wave_create()

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
