from django.db import models


class RemoteGPIOController(models.Model):
    RASPBERRY_PI_CONTROLLER = 'PI'
    ARDUINO_CONTROLLER = 'AR'
    FAKE_CONTROLLER = 'FA'

    CONTROLLER_TYPE = [
        (RASPBERRY_PI_CONTROLLER, 'Raspberry Pi Controller (pigpio)'),
        (ARDUINO_CONTROLLER, 'Arduino Controller'),
        (FAKE_CONTROLLER, 'Fake Controller'),
    ]

    name = models.CharField(max_length=50)

    hostname = models.CharField(max_length=50)
    port = models.IntegerField()
    controller_type = models.CharField(max_length=2, choices=CONTROLLER_TYPE, default=RASPBERRY_PI_CONTROLLER)

    def __str__(self):
        return "GPIO Controller ({})".format(self.name)


class AddressableLEDStrip(models.Model):
    WS2801 = 'WS'

    ADDRESSABLE_LED_TYPE = [
        (WS2801, 'WS2801 Controller')
    ]

    controller = models.ForeignKey("RemoteGPIOController", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    led_count = models.IntegerField()

    spi_device = models.IntegerField()
    controller_type = models.CharField(max_length=2, choices=ADDRESSABLE_LED_TYPE, default=WS2801)

    def __str__(self):
        return "Addressable LED Strip ({})".format(self.name)


class LEDStrip(models.Model):
    controller = models.ForeignKey("RemoteGPIOController", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    red_pin = models.IntegerField()
    green_pin = models.IntegerField()
    blue_pin = models.IntegerField()

    def __str__(self):
        return "LED Strip ({})".format(self.name)


class WirelessTransmitter(models.Model):
    controller = models.ForeignKey("RemoteGPIOController", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pin = models.IntegerField()

    def __str__(self):
        return "Transmitter ({})".format(self.name)


class RemoteSocket(models.Model):
    transmitter = models.ForeignKey("WirelessTransmitter", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    group = models.CharField(max_length=50)
    device = models.CharField(max_length=50)
    repeats = models.IntegerField()

    def __str__(self):
        return "Remote Socket ({})".format(self.name)
