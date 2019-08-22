from django.contrib import admin

from device_controller_api.models import LedStripModel, RemoteSocketModel, AddressableLedStripModel, \
    GpioControllerModel, PigpioGpioControllerModel, WS2801AddressableLedStripModel, RGBLedStripModel, \
    ErloRemoteSocketModel

admin.site.register(GpioControllerModel)
admin.site.register(PigpioGpioControllerModel)

admin.site.register(AddressableLedStripModel)
admin.site.register(WS2801AddressableLedStripModel)

admin.site.register(LedStripModel)
admin.site.register(RGBLedStripModel)

admin.site.register(RemoteSocketModel)
admin.site.register(ErloRemoteSocketModel)
