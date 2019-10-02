from django.db import models

from devices.models import Device


class Room(models.Model):
    name = models.CharField(max_length=50)
    devices = models.ManyToManyField(Device)
    icon_url = models.URLField()

    def __str__(self):
        return "Room ({})".format(self.name)
