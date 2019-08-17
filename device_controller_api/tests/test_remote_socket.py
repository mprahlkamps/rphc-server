from django.test import TestCase

from device_controller_api.models import RemoteSocket, Transmitter, RemoteGPIOController


class RemoteSocketTestCase(TestCase):

    def setUp(self):
        controller = RemoteGPIOController.objects.create(name="controller", hostname="localhost", port=8888,
                                                         controller_type=RemoteGPIOController.FAKE_CONTROLLER)
        controller.save()

        self.transmitter = Transmitter.objects.create(controller=controller, pin=17, retries=10)
        self.transmitter.save()

    def test_create_remote_socket(self):
        try:
            remote_socket = RemoteSocket.objects.create(transmitter=self.transmitter,
                                                        name="test_socket",
                                                        group="10000",
                                                        device="10000")
            remote_socket.save()
        except Exception as e:
            self.fail(e)

    def test_remote_socket_str(self):
        remote_socket = RemoteSocket.objects.create(transmitter=self.transmitter,
                                                    name="test_socket",
                                                    group="10000",
                                                    device="10000")

        self.assertEquals(str(remote_socket), "Remote Socket (test_socket)")
