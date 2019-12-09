from django.contrib import admin

from devices.models import PiGPIO, WS2801AddressableLedStrip, RGBLedStrip, \
    ErloRemoteSocket, SonoffRemoteSocket

admin.site.register(PiGPIO)
admin.site.register(WS2801AddressableLedStrip)
admin.site.register(RGBLedStrip)
admin.site.register(ErloRemoteSocket)
admin.site.register(SonoffRemoteSocket)
