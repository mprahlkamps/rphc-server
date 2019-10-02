from django.db import models
from polymorphic.models import PolymorphicModel


#
# Device models
#
class Device(PolymorphicModel):
    name = models.CharField(max_length=50)


class AddressableLedStrip(Device):
    pass


class LedStrip(Device):
    pass


class RemoteSocket(Device):
    pass


class WS2801AddressableLedStrip(AddressableLedStrip):
    controller = models.ForeignKey("PiGPIO", on_delete=models.CASCADE)
    total_led_count = models.PositiveIntegerField()
    usable_led_count = models.PositiveIntegerField()
    spi_channel = models.PositiveIntegerField()
    spi_frequency = models.PositiveIntegerField()

    def __str__(self):
        return "WS2801 Addressable LED Strip ({})".format(self.name)

    class Meta:
        verbose_name = 'WS2801 Addressable Led Strip'
        verbose_name_plural = 'WS2801 Addressable Led Strips'


class RGBLedStrip(LedStrip):
    controller = models.ForeignKey("PiGPIO", on_delete=models.CASCADE)
    red_pin = models.PositiveIntegerField()
    green_pin = models.PositiveIntegerField()
    blue_pin = models.PositiveIntegerField()

    def __str__(self):
        return "RGB LED Strip ({})".format(self.name)

    class Meta:
        verbose_name = 'RGB Led Strip'
        verbose_name_plural = 'RGB Led Strips'


class ErloRemoteSocket(RemoteSocket):
    controller = models.ForeignKey("PiGPIO", on_delete=models.CASCADE)
    transmitter_pin = models.PositiveIntegerField()
    group_code = models.CharField(max_length=50)
    device_code = models.CharField(max_length=50)
    repeats = models.PositiveIntegerField()

    def __str__(self):
        return "Erlo Remote Socket ({})".format(self.name)

    class Meta:
        verbose_name = 'Erlo Remote Socket'
        verbose_name_plural = 'Erlo Remote Sockets'


class SonoffRemoteSocket(RemoteSocket):
    ip = models.CharField(max_length=50)
    port = models.PositiveIntegerField()
    device_id = models.CharField(max_length=50)

    def __str__(self):
        return "Sonoff Remote Socket ({})".format(self.name)

    class Meta:
        verbose_name = 'Sonoff Remote Socket'
        verbose_name_plural = 'Sonoff Remote Sockets'


#
# GPIO controller models
#
class Controller(PolymorphicModel):
    name = models.CharField(max_length=50)


class PiGPIO(Controller):
    hostname = models.CharField(max_length=50)
    port = models.PositiveIntegerField()

    def __str__(self):
        return "PiGPIO controller ({})".format(self.name)

    class Meta:
        verbose_name = 'PiGPIO'
        verbose_name_plural = 'PiGPIOs'
