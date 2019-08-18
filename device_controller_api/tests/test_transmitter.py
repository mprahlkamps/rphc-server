from django.test import TestCase

from device_controller_api.models import WirelessTransmitter, RemoteGPIOController


class TransmitterTestCase(TestCase):

    def setUp(self):
        self.controller = RemoteGPIOController.objects.create(name="controller", hostname="localhost", port=8888,
                                                              type=RemoteGPIOController.FAKE_CONTROLLER)

    def test_create_transmitter(self):
        try:
            WirelessTransmitter.objects.create(controller=self.controller,
                                               name="Transmitter",
                                               pin=17)
        except Exception as e:
            self.fail(e)

    def test_transmitter_str(self):
        transmitter = WirelessTransmitter.objects.create(controller=self.controller,
                                                         name="Transmitter",
                                                         pin=17)
        self.assertEqual(str(transmitter), "Transmitter (Transmitter)")
