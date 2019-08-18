from django.test import TestCase

from device_controller_api.models import RemoteSocket, WirelessTransmitter, RemoteGPIOController


class RemoteSocketTestCase(TestCase):

    def setUp(self):
        controller = RemoteGPIOController.objects.create(name="controller", hostname="localhost", port=8888,
                                                         type=RemoteGPIOController.FAKE_CONTROLLER)
        controller.save()

        self.transmitter = WirelessTransmitter.objects.create(controller=controller, name="Transmitter", pin=17)
        self.transmitter.save()

    def test_create_remote_socket(self):
        try:
            remote_socket = RemoteSocket.objects.create(transmitter=self.transmitter,
                                                        name="test_socket",
                                                        group="10000",
                                                        device="10000",
                                                        repeats=10)
            remote_socket.save()
        except Exception as e:
            self.fail(e)

    def test_remote_socket_str(self):
        remote_socket = RemoteSocket.objects.create(transmitter=self.transmitter,
                                                    name="test_socket",
                                                    group="10000",
                                                    device="10000",
                                                    repeats=10)

        self.assertEquals(str(remote_socket), "Remote Socket (test_socket)")
