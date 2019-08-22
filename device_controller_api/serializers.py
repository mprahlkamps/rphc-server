from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from device_controller_api.models import LedStripModel, RemoteSocketModel, \
    AddressableLedStripModel, GpioControllerModel, PigpioGpioControllerModel, WS2801AddressableLedStripModel, \
    ErloRemoteSocketModel, RGBLedStripModel


#
# Base serializers
#
class GpioControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpioControllerModel
        fields = ('id', 'name')


class AddressableLedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressableLedStripModel
        fields = ('id', 'name')


class LedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedStripModel
        fields = ('id', 'name')


class RemoteSocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteSocketModel
        fields = ('id', 'name')


#
# Concrete serializers
#
class PigpioGpioControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PigpioGpioControllerModel
        fields = ('id', 'name', 'hostname', 'port')


class WS2801AddressableLedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = WS2801AddressableLedStripModel
        fields = (
        'id', 'name', 'gpio_controller', 'total_led_count', 'usable_led_count', 'spi_channel', 'spi_frequency')


class RGBLedStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RGBLedStripModel
        fields = ('id', 'name', 'gpio_controller', 'red_pin', 'green_pin', 'blue_pin')


class ErloRemoteSocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErloRemoteSocketModel
        fields = ('id', 'name', 'gpio_controller', 'transmitter_pin', 'group_code', 'device_code', 'repeats')


#
# Polymorphic Serializers
#
class GpioControllerPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        GpioControllerModel: GpioControllerSerializer,
        PigpioGpioControllerModel: PigpioGpioControllerSerializer
    }


class AddressableLedStripPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        AddressableLedStripModel: AddressableLedStripSerializer,
        WS2801AddressableLedStripModel: WS2801AddressableLedStripSerializer
    }


class LedStripPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        LedStripModel: LedStripSerializer,
        RGBLedStripModel: RGBLedStripSerializer
    }


class RemoteSocketPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        RemoteSocketModel: RemoteSocketSerializer,
        ErloRemoteSocketModel: ErloRemoteSocketSerializer
    }
