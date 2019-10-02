from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from devices.models import LedStrip, RemoteSocket, \
    AddressableLedStrip, Controller, PiGPIO, WS2801AddressableLedStrip, \
    ErloRemoteSocket, RGBLedStrip, Device


#
# Devices
#
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name')


class AddressableLedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressableLedStrip
        fields = ('id', 'name')


class LedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedStrip
        fields = ('id', 'name')


class RemoteSocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteSocket
        fields = ('id', 'name')


class WS2801AddressableLedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = WS2801AddressableLedStrip
        fields = ('id', 'name', 'controller', 'total_led_count', 'usable_led_count', 'spi_channel',
                  'spi_frequency')


class RGBLedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RGBLedStrip
        fields = ('id', 'name', 'controller', 'red_pin', 'green_pin', 'blue_pin')


class ErloRemoteSocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErloRemoteSocket
        fields = ('id', 'name', 'controller', 'transmitter_pin', 'group_code', 'device_code', 'repeats')


#
# GPIO Controller
#
class GpioControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controller
        fields = ('id', 'name')


class PigpioGpioControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiGPIO
        fields = ('id', 'name', 'hostname', 'port')


#
# Polymorphic Serializers
#
class DevicePolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Device: DeviceSerializer,
        PiGPIO: PigpioGpioControllerSerializer,
        WS2801AddressableLedStrip: WS2801AddressableLedStripSerializer,
        RGBLedStrip: RGBLedStripSerializer,
        ErloRemoteSocket: ErloRemoteSocketSerializer
    }


class GpioControllerPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Controller: GpioControllerSerializer,
        PiGPIO: PigpioGpioControllerSerializer
    }


class AddressableLedStripPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        AddressableLedStrip: AddressableLedStripSerializer,
        WS2801AddressableLedStrip: WS2801AddressableLedStripSerializer
    }


class LedStripPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        LedStrip: LedStripSerializer,
        RGBLedStrip: RGBLedStripSerializer
    }


class RemoteSocketPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        RemoteSocket: RemoteSocketSerializer,
        ErloRemoteSocket: ErloRemoteSocketSerializer
    }
