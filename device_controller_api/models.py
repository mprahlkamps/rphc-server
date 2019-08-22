from django.db import models

# Base models
from polymorphic.models import PolymorphicModel


class GpioControllerModel(PolymorphicModel):
    name = models.CharField(max_length=50)


class AddressableLedStripModel(PolymorphicModel):
    name = models.CharField(max_length=50)


class LedStripModel(PolymorphicModel):
    name = models.CharField(max_length=50)


class RemoteSocketModel(PolymorphicModel):
    name = models.CharField(max_length=50)


# Concrete models
class PigpioGpioControllerModel(GpioControllerModel):
    hostname = models.CharField(max_length=50)
    port = models.PositiveIntegerField()

    def __str__(self):
        return "pigpio GPIO Controller ({})".format(self.name)


class WS2801AddressableLedStripModel(AddressableLedStripModel):
    gpio_controller = models.ForeignKey("PigpioGpioControllerModel", on_delete=models.CASCADE)
    total_led_count = models.PositiveIntegerField()
    usable_led_count = models.PositiveIntegerField()
    spi_channel = models.PositiveIntegerField()
    spi_frequency = models.PositiveIntegerField()

    def __str__(self):
        return "WS2801 Addressable LED Strip ({})".format(self.name)


class RGBLedStripModel(LedStripModel):
    gpio_controller = models.ForeignKey("PigpioGpioControllerModel", on_delete=models.CASCADE)
    red_pin = models.PositiveIntegerField()
    green_pin = models.PositiveIntegerField()
    blue_pin = models.PositiveIntegerField()

    def __str__(self):
        return "RGB LED Strip ({})".format(self.name)


class ErloRemoteSocketModel(RemoteSocketModel):
    gpio_controller = models.ForeignKey("PigpioGpioControllerModel", on_delete=models.CASCADE)
    transmitter_pin = models.PositiveIntegerField()
    group_code = models.CharField(max_length=50)
    device_code = models.CharField(max_length=50)
    repeats = models.PositiveIntegerField()

    def __str__(self):
        return "Erlo Remote Socket ({})".format(self.name)
