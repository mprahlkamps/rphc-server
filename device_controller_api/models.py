from django.db import models


class RemoteGPIOController(models.Model):
    PIGPIO_CONTROLLER = 'PI'
    ARDUINO_CONTROLLER = 'AR'
    FAKE_CONTROLLER = 'FA'

    CONTROLLER_TYPE = [
        (PIGPIO_CONTROLLER, 'PIGPIO Controller'),
        (ARDUINO_CONTROLLER, 'Arduino Controller'),
        (FAKE_CONTROLLER, 'Fake Controller'),
    ]

    name = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    port = models.IntegerField()
    controller_type = models.CharField(max_length=2, choices=CONTROLLER_TYPE, default=PIGPIO_CONTROLLER)

    def __str__(self):
        return "GPIO Controller ({})".format(self.name)


class AddressableLEDStrip(models.Model):
    controller = models.ForeignKey("RemoteGPIOController", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    spi_device = models.IntegerField()
    led_count = models.IntegerField()

    def __str__(self):
        return "Addressable LED Strip ({})".format(self.spi_device)


class LEDStrip(models.Model):
    controller = models.ForeignKey("RemoteGPIOController", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    red_pin = models.IntegerField()
    green_pin = models.IntegerField()
    blue_pin = models.IntegerField()

    def __str__(self):
        return "LED Strip ({},{},{})".format(self.red_pin, self.green_pin, self.blue_pin)


class Transmitter(models.Model):
    controller = models.ForeignKey("RemoteGPIOController", on_delete=models.CASCADE)
    pin = models.IntegerField()
    retries = models.IntegerField()

    def __str__(self):
        return "Transmitter ({})".format(self.pin)


class RemoteSocket(models.Model):
    transmitter = models.ForeignKey("Transmitter", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    device = models.CharField(max_length=50)

    def __str__(self):
        return "Remote Socket ({})".format(self.name)
