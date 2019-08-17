from django.test import TestCase

from device_controller_api.models import Controller


class ControllerTestCase(TestCase):

    def test_create_controller(self):
        try:
            controller = Controller.objects.create(name="controller", hostname="localhost", port=8888)
            controller.save()
        except Exception as e:
            self.fail(e)

    def test_controller_str(self):
        controller = Controller.objects.create(name="controller", hostname="localhost", port=8888)
        self.assertEqual(str(controller), "Controller (localhost:8888)")

        controller = Controller.objects.create(name="controller", hostname="test", port=1234)
        self.assertEqual(str(controller), "Controller (test:1234)")
