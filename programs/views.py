from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from programs.programs.program_manager import ProgramManager


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
