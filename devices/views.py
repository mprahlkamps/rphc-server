from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from devices.controller.controller_manager import ControllerManager
from devices.models import RemoteSocket, Controller, AddressableLedStrip, LedStrip, Device
from devices.serializers import GpioControllerPolymorphicSerializer, \
    AddressableLedStripPolymorphicSerializer, RemoteSocketPolymorphicSerializer, LedStripPolymorphicSerializer, \
    DevicePolymorphicSerializer


class ControllerViewSet(viewsets.ModelViewSet):
    queryset = Controller.objects.all()
    serializer_class = GpioControllerPolymorphicSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DevicePolymorphicSerializer


class AddressableLedStripViewSet(viewsets.ModelViewSet):
    queryset = AddressableLedStrip.objects.all()
    serializer_class = AddressableLedStripPolymorphicSerializer

    @action(detail=True, methods=['post'], url_path='set-color')
    def set_color(self, request, pk):
        color_data = request.data
        color = (int(color_data['r']), int(color_data['g']), int(color_data['b']))

        # TODO: Add checks

        led_strip_controller = ControllerManager.get_addressable_led_strip_controller(pk)
        led_strip_controller.set_color(color)
        led_strip_controller.show()

        return Response({'msg': 'Set color {}'.format(color)})


class LedStripViewSet(viewsets.ModelViewSet):
    queryset = LedStrip.objects.all()
    serializer_class = LedStripPolymorphicSerializer

    @action(detail=True, methods=['post'])
    def set_color(self, request, pk):
        color_data = request.data
        color = (int(color_data['r']), int(color_data['g']), int(color_data['b']))

        # TODO: Add checks

        led_strip_controller = ControllerManager.get_led_strip_controller(pk)
        led_strip_controller.set_color(color)

        return Response({'msg': 'Set color {}'.format(color)})


class RemoteSocketViewSet(viewsets.ModelViewSet):
    queryset = RemoteSocket.objects.all()
    serializer_class = RemoteSocketPolymorphicSerializer

    @action(detail=True, methods=['post'])
    def enable(self, request, pk):
        socket_controller = ControllerManager.get_remote_socket_controller(pk)
        socket_controller.enable()

        return Response({'msg': 'Enabled remote socket'})

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        socket_controller = ControllerManager.get_remote_socket_controller(pk)
        socket_controller.disable()

        return Response({'msg': 'Disabled remote socket'})

    @action(detail=True, methods=['get'])
    def status(self, request, pk):
        socket_controller = ControllerManager.get_remote_socket_controller(pk)

        try:
            status = socket_controller.status()
        except NotImplementedError:
            return Response({'error': True, 'msg': 'Status not available'})

        return Response({'status': status})
