from colorful.fields import RGBColorField
from django.core.exceptions import ValidationError
from django.db import models
from polymorphic.models import PolymorphicModel

from devices.models import Device, SonoffRemoteSocket, ErloRemoteSocket, RGBLedStrip, \
    WS2801AddressableLedStrip


def validate_remote_socket(device_id):
    device = Device.objects.get(id=device_id)
    if type(device) not in (SonoffRemoteSocket, ErloRemoteSocket):
        raise ValidationError("Only applicable to Remote Sockets")


def validate_led_strip(device_id):
    device = Device.objects.get(id=device_id)
    if type(device) not in (RGBLedStrip, WS2801AddressableLedStrip):
        raise ValidationError("Only applicable to LED Strips")


class Action(PolymorphicModel):
    pass


class EnableRemoteSocketAction(Action):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, validators=[validate_remote_socket])

    def __str__(self):
        return f"Enable {self.device}"


class DisableRemoteSocketAction(Action):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, validators=[validate_remote_socket])

    def __str__(self):
        return f"Disable {self.device}"


class SetLedStripColorAction(Action):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, validators=[validate_led_strip])
    color = RGBColorField()

    def __str__(self):
        return f"Set {self.device} to {self.color}"


class Scene(models.Model):
    name = models.CharField(max_length=50)
    actions = models.ManyToManyField(Action)

    def __str__(self):
        return f"Scene ({self.name})"
