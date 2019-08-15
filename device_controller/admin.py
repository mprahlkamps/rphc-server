from django.contrib import admin

from device_controller.models import AddressableLEDStrip, LEDStrip, RemoteSocket, Transmitter, Controller

admin.site.register(Controller)
admin.site.register(AddressableLEDStrip)
admin.site.register(LEDStrip)
admin.site.register(RemoteSocket)
admin.site.register(Transmitter)
