from django.db import models


class Controller(models.Model):
    name = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    port = models.IntegerField()

    def __str__(self):
        return "RaspberryPi ({}:{})".format(self.hostname, self.port)


class AddressableLEDStrip(models.Model):
    controller = models.ForeignKey("Controller", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    spi_device = models.IntegerField()
    led_count = models.IntegerField()

    def __str__(self):
        return "Addressable LED Strip ({})".format(self.spi_device)


class LEDStrip(models.Model):
    controller = models.ForeignKey("Controller", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    red_pin = models.IntegerField()
    green_pin = models.IntegerField()
    blue_pin = models.IntegerField()

    def __str__(self):
        return "LED Strip ({},{},{})".format(self.red_pin, self.green_pin, self.blue_pin)


class Transmitter(models.Model):
    controller = models.ForeignKey("Controller", on_delete=models.CASCADE)
    pin = models.IntegerField()
    retries = models.IntegerField()

    def __str__(self):
        return "Remote Socket Transmitter ({})".format(self.pin)


class RemoteSocket(models.Model):
    transmitter = models.ForeignKey("Transmitter", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    device = models.CharField(max_length=50)

    def __str__(self):
        return "Remote Socket ({})".format(self.name)
