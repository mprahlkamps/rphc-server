from django.test import TestCase

from authentication.apps import AuthenticationConfig
from devices.apps import DeviceControllerConfig
from programs.apps import ProgramApiConfig


class AppConfigTest(TestCase):

    def test_app_configs(self):
        self.assertEqual(AuthenticationConfig.name, "authentication")
        self.assertEqual(DeviceControllerConfig.name, "devices")
        self.assertEqual(ProgramApiConfig.name, "programs")
