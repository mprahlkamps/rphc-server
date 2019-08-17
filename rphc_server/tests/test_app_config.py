from django.test import TestCase

from authentication.apps import AuthenticationConfig
from authentication.models import User
from device_controller_api.apps import DeviceControllerConfig
from program_api.apps import ProgramApiConfig


class AppConfigTest(TestCase):

    def test_app_configs(self):
        self.assertEqual(AuthenticationConfig.name, "authentication")
        self.assertEqual(DeviceControllerConfig.name, "device_controller_api")
        self.assertEqual(ProgramApiConfig.name, "program_api")
