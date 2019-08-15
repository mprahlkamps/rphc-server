import colorsys

from device_controller_api.controller.controller_manager import ControllerManager
from program_api.programs.program_plugin import ProgramPlugin


class LEDFader(ProgramPlugin):

    def __init__(self):
        self.controller = ControllerManager.get_addressable_led_strip_controller(1)

        self.current_color = [255, 0, 0]
        self.start_color = [255, 0, 0]
        self.end_color = [255, 0, 0]

        self.current_delta = 0.0

    def update(self, seconds, delta):
        if self.current_color != self.end_color and self.current_delta <= 1:
            self.current_color = LEDFader.interpolate_color(self.start_color, self.end_color, self.current_delta)

            self.controller.set_color_all(self.current_color[0], self.current_color[1], self.current_color[2])
            self.controller.show()

            self.current_delta += delta
        else:
            pass

    def get_info(self):
        pass

    def set_variables(self, variables):
        if 'color' in variables:
            self.end_color = [variables['color']['r'],
                              variables['color']['g'],
                              variables['color']['b']]

            self.start_color = self.current_color
            self.current_delta = 0.0

    def on_start(self):
        self.controller.set_color_all(self.current_color[0], self.current_color[1], self.current_color[2])
        self.controller.show()

    def on_stop(self):
        pass

    @staticmethod
    def hsv_to_rgb(h, s, v):
        rgb = colorsys.hsv_to_rgb(h, s, v)
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        return r, g, b

    @staticmethod
    def interpolate_color(color_a, color_b, delta):
        return [int(a + (b - a) * delta) for a, b in zip(color_a, color_b)]
