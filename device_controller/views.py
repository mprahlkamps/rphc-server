from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from device_controller.controller.controller_manager import ControllerManager
from device_controller.models import AddressableLEDStrip, RemoteSocket, Transmitter, Controller
from device_controller.programs.program_manager import ProgramManager
from device_controller.serializers import AddressableLedStripSerializer, RemoteSocketSerializer, \
    TransmitterSerializer, ControllerSerializer


class ControllerViewSet(viewsets.ModelViewSet):
    queryset = Controller.objects.all()
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


class ListPrograms(GenericAPIView):
    @staticmethod
    def get(request):
        return Response({'programs': ProgramManager.get_program_list()})


class StartProgram(GenericAPIView):

    @staticmethod
    def post(request):
        params = request.query_params
        name = params['name']
        ProgramManager.start_program(name)
        return Response({'msg': 'Starting program {}'.format(name)})


class StopProgram(GenericAPIView):
    @staticmethod
    def post(request):
        ProgramManager.stop_program()
        return Response({'msg': 'Stopping program'})


class RestartProgram(GenericAPIView):
    @staticmethod
    def post(request):
        return Response({'msg': 'Restarting program'})


class SetProgramVariables(GenericAPIView):
    @staticmethod
    def post(request):
        ProgramManager.set_variables(request.data)
        return Response({'msg': 'Setting program variables'})


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
