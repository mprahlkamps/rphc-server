from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from device_controller_api.controller.controller_manager import ControllerManager
from device_controller_api.models import RemoteSocketModel, GpioControllerModel, AddressableLedStripModel, LedStripModel
from device_controller_api.serializers import GpioControllerPolymorphicSerializer, \
    AddressableLedStripPolymorphicSerializer, RemoteSocketPolymorphicSerializer, LedStripPolymorphicSerializer


class GpioControllerViewSet(viewsets.ModelViewSet):
    queryset = GpioControllerModel.objects.all()
    serializer_class = GpioControllerPolymorphicSerializer


class AddressableLedStripViewSet(viewsets.ModelViewSet):
    queryset = AddressableLedStripModel.objects.all()
    serializer_class = AddressableLedStripPolymorphicSerializer


class LedStripViewSet(viewsets.ModelViewSet):
    queryset = LedStripModel.objects.all()
    serializer_class = LedStripPolymorphicSerializer


class RemoteSocketViewSet(viewsets.ModelViewSet):
    queryset = RemoteSocketModel.objects.all()
    serializer_class = RemoteSocketPolymorphicSerializer


class SetAddressableLedStripColor(GenericAPIView):
    @staticmethod
    def post(request, **kwargs):
        led_strip_id = kwargs['pk']
        color_data = request.data
        color = (int(color_data['r']), int(color_data['g']), int(color_data['b']))

        # TODO: Add checks

        led_strip_controller = ControllerManager.get_addressable_led_strip_controller(led_strip_id)
        led_strip_controller.set_color(color)
        led_strip_controller.show()

        return Response({'msg': 'Set color {}'.format(color)})


class EnableRemoteSocket(GenericAPIView):
    @staticmethod
    def post(request, *args, **kwargs):
        socket_id = kwargs['pk']

        socket_controller = ControllerManager.get_remote_socket_controller(socket_id)
        socket_controller.enable()

        return Response({'msg': 'Enabled remote socket'})


class DisableRemoteSocket(GenericAPIView):
    @staticmethod
    def post(request, *args, **kwargs):
        socket_id = kwargs['pk']

        socket_controller = ControllerManager.get_remote_socket_controller(socket_id)
        socket_controller.disable()

        return Response({'msg': 'Disabled remote socket'})
