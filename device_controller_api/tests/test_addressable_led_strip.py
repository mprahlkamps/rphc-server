from django.test import TestCase

from device_controller_api.models import AddressableLEDStrip, RemoteGPIOController


class AddressableLEDStripTestCase(TestCase):

    def setUp(self):
        self.controller = RemoteGPIOController.objects.create(name="controller", hostname="localhost", port=8888,
                                                              controller_type=RemoteGPIOController.FAKE_CONTROLLER)
        self.controller.save()

    def test_create_addressable_led_strip(self):
        try:
            led_strip = AddressableLEDStrip.objects.create(controller=self.controller,
                                                           name="Addressable LED Strip",
                                                           spi_device=0,
                                                           led_count=200,
                                                           usable_led_count=89)
            led_strip.save()
        except Exception as e:
            self.fail(e)

    def test_addressable_led_strip_str(self):
        led_strip = AddressableLEDStrip.objects.create(controller=self.controller,
                                                       name="Addressable LED Strip",
                                                       spi_device=0,
                                                       led_count=200,
                                                       usable_led_count=98)

        self.assertEqual(str(led_strip), "Addressable LED Strip (Addressable LED Strip)")
