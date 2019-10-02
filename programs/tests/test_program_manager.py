from django.test import TestCase

from programs.programs.program_manager import ProgramManager


class ProgramManagerTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_program_list(self):
        result = ProgramManager.get_program_list()
        self.assertTrue('LEDFader' in result)
        self.assertFalse('' in result)
