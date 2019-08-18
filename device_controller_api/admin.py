from django.contrib import admin

from device_controller_api.models import AddressableLEDStrip, LEDStrip, RemoteSocket, WirelessTransmitter, \
    RemoteGPIOController

admin.site.register(RemoteGPIOController)
admin.site.register(AddressableLEDStrip)
admin.site.register(LEDStrip)
admin.site.register(RemoteSocket)
admin.site.register(WirelessTransmitter)
