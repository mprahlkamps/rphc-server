from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from device_controller_api.controller.controller_manager import ControllerManager
from device_controller_api.models import AddressableLEDStrip, RemoteSocket, WirelessTransmitter, RemoteGPIOController
from device_controller_api.serializers import AddressableLedStripSerializer, RemoteSocketSerializer, \
    WirelessTransmitterSerializer, ControllerSerializer


class ControllerViewSet(viewsets.ModelViewSet):
    queryset = RemoteGPIOController.objects.all()
    serializer_class = ControllerSerializer


class AddressableLedStripViewSet(viewsets.ModelViewSet):
    queryset = AddressableLEDStrip.objects.all()
    serializer_class = AddressableLedStripSerializer


class RemoteSocketViewSet(viewsets.ModelViewSet):
    queryset = RemoteSocket.objects.all()
    serializer_class = RemoteSocketSerializer


class TransmitterViewSet(viewsets.ModelViewSet):
    queryset = WirelessTransmitter.objects.all()
    serializer_class = WirelessTransmitterSerializer


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
