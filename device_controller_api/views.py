from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from device_controller_api.controller.controller_manager import ControllerManager
from device_controller_api.models import AddressableLEDStrip, RemoteSocket, Transmitter, RemoteGPIOController
from device_controller_api.serializers import AddressableLedStripSerializer, RemoteSocketSerializer, \
    TransmitterSerializer, ControllerSerializer


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
    queryset = Transmitter.objects.all()
    serializer_class = TransmitterSerializer


class SetAddressableLedStripColor(GenericAPIView):
    @staticmethod
    def post(request, **kwargs):
        led_strip_id = kwargs['pk']
        color = request.data

        led_strip_controller = ControllerManager.get_addressable_led_strip_controller(led_strip_id)
        led_strip_controller.set_color_all(int(color['r']), int(color['g']), int(color['b']))
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
