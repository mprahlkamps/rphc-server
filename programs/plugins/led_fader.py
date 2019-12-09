import colorsys
from typing import Tuple

from devices.controller.controller_manager import ControllerManager
from programs.programs.program_plugin import ProgramPlugin


class LEDFader(ProgramPlugin):

    def __init__(self):
        self.controller = ControllerManager.get_addressable_led_strip_controller(1)

        self.current_color = (255, 0, 0)
        self.start_color = (255, 0, 0)
        self.end_color = (255, 0, 0)

        self.current_delta = 0.0

    def update(self, seconds, delta):
        if self.current_color != self.end_color and self.current_delta <= 1:
            self.current_color = LEDFader.interpolate_color(self.start_color, self.end_color, self.current_delta)

            self.controller.set_color(self.current_color)
            self.controller.show()

            self.current_delta += delta
        else:
            pass

    def get_info(self):
        pass

    def set_variables(self, variables):
        if 'color' in variables:
            self.end_color = (variables['color']['r'],
                              variables['color']['g'],
                              variables['color']['b'])

            self.start_color = self.current_color
            self.current_delta = 0.0

    def on_start(self):
        self.controller.set_color(self.current_color)
        self.controller.show()

    def on_stop(self):
        pass

    @staticmethod
    def hsv_to_rgb(hsv_color: Tuple[int, int, int]):
        h, s, v = hsv_color
        rgb = colorsys.hsv_to_rgb(h, s, v)
        rgb[0] = int(rgb[0] * 255)
        rgb[1] = int(rgb[1] * 255)
        rgb[2] = int(rgb[2] * 255)
        return rgb

    @staticmethod
    def interpolate_color(color_a: Tuple[int, int, int], color_b: Tuple[int, int, int], delta) -> Tuple[int, int, int]:
        color = (int(color_a[0] + (color_b[0] - color_a[0]) * delta),
                 int(color_a[1] + (color_b[1] - color_a[1]) * delta),
                 int(color_a[2] + (color_b[2] - color_a[2]) * delta))
        return color
