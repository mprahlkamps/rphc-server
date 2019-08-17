from rest_framework import serializers

from device_controller_api.models import AddressableLEDStrip, LEDStrip, RemoteSocket, Transmitter, RemoteGPIOController


class ControllerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemoteGPIOController
        fields = ('id', 'name', 'hostname', 'port')


class AddressableLedStripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressableLEDStrip
        fields = ('id', 'name', 'controller', 'spi_device', 'led_count')


class LedStripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LEDStrip
        fields = ('id', 'name', 'controller', 'red_pin', 'green_pin', 'blue_pin')


class RemoteSocketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemoteSocket
        fields = ('id', 'name', 'transmitter', 'group', 'device')


class TransmitterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transmitter
        fields = ('id', 'controller', 'pin')
