from django.core.management import BaseCommand

from device_controller_api.models import RemoteGPIOController, WirelessTransmitter, RemoteSocket, AddressableLEDStrip


class Command(BaseCommand):
    help = "email: admin@admin.de, pw: admin"

    def handle(self, *args, **options):
        gpio_controller = RemoteGPIOController.objects.create(name="Raspberry Pi Zero",
                                                              hostname="raspberrypi-zero",
                                                              port=8888,
                                                              type=RemoteGPIOController.RASPBERRY_PI_CONTROLLER)

        transmitter = WirelessTransmitter.objects.create(name="433 MHz",
                                                         controller=gpio_controller,
                                                         pin=17)

        RemoteSocket.objects.create(name="Test Socket 1",
                                    transmitter=transmitter,
                                    group="100000",
                                    device="100000",
                                    repeats=20)

        AddressableLEDStrip.objects.create(name="Addressable LEDs",
                                           controller=gpio_controller,
                                           led_count=160,
                                           usable_led_count=89,
                                           spi_device=0,
                                           type=AddressableLEDStrip.WS2801)
