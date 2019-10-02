# class RemoteSocketTestCase(TestCase):
#
#     def setUp(self):
#         self.controller = PigpioGpioControllerModel.objects.create(name="controller", hostname="localhost", port=8888)
#
#     def test_create_remote_socket(self):
#         try:
#             RemoteSocketModel.objects.create(gpio_controller=self.controller,
#                                              name="test_socket",
#                                              transmitter_pin=17,
#                                              group="10000",
#                                              device="10000",
#                                              repeats=10)
#         except Exception as e:
#             self.fail(e)
#
#     def test_remote_socket_str(self):
#         remote_socket = RemoteSocketModel.objects.create(gpio_controller=self.controller,
#                                                          name="test_socket",
#                                                          transmitter_pin=17,
#                                                          group="10000",
#                                                          device="10000",
#                                                          repeats=10)
#
#         self.assertEquals(str(remote_socket), "Remote Socket (test_socket)")
