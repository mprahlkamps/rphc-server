from rest_framework import serializers

from device_controller_api.models import AddressableLEDStrip, LEDStrip, RemoteSocket, WirelessTransmitter, \
    RemoteGPIOController


class ControllerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemoteGPIOController
        fields = ('id', 'name', 'hostname', 'port')


class AddressableLedStripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressableLEDStrip
        fields = ('id', 'name', 'controller', 'spi_device', 'led_count', 'usable_led_count')


class LedStripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LEDStrip
        fields = ('id', 'name', 'controller', 'red_pin', 'green_pin', 'blue_pin')


class RemoteSocketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemoteSocket
        fields = ('id', 'name', 'transmitter', 'group', 'device', 'repeats')


class WirelessTransmitterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WirelessTransmitter
        fields = ('id', 'controller', 'pin')
