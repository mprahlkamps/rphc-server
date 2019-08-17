from django.test import TestCase

from device_controller_api.models import Controller, Transmitter


class TransmitterTestCase(TestCase):

    def setUp(self):
        self.controller = Controller.objects.create(name="controller", hostname="localhost", port=8888)
        self.controller.save()

    def test_create_transmitter(self):
        try:
            transmitter = Transmitter.objects.create(controller=self.controller,
                                                     pin=17,
                                                     retries=10)
            transmitter.save()
        except Exception as e:
            self.fail(e)

    def test_transmitter_str(self):
        transmitter = Transmitter.objects.create(controller=self.controller,
                                                 pin=17,
                                                 retries=10)
        self.assertEqual(str(transmitter), "Transmitter (17)")

        transmitter = Transmitter.objects.create(controller=self.controller,
                                                 pin=20,
                                                 retries=10)
        self.assertEqual(str(transmitter), "Transmitter (20)")
