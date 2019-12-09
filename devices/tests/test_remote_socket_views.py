# class RemoteSocketViewTestCase(TestCase):
#
#     def setUp(self):
#         user = User.objects.create_user("admin@admin.de", "admin")
#         controller = PigpioGpioControllerModel.objects.create(name="controller", hostname="localhost", port=8888)
#         socket = RemoteSocketModel.objects.create(gpio_controoler=controller, name="led",
#                                                   transmitter_pin=17,
#                                                   group_code="000000", device_code="000000",
#                                                   repeats=10)
#
#         self.client = Client()
#         response = self.client.post("/api/auth/token/", {"email": "admin@admin.de", "password": "admin"})
#         self.access_token = json.loads(response.content.decode('utf-8'))['access']
#
#     def test_list_remote_socket(self):
#         resp = self.client.get("/api/devices/remote-socket/",
#                                HTTP_AUTHORIZATION='Bearer ' + self.access_token)
#
#         self.assertEqual(resp.status_code, 200)
#
#     def test_list_detail_remote_socket(self):
#         resp = self.client.get("/api/devices/remote-socket/1/",
#                                HTTP_AUTHORIZATION='Bearer ' + self.access_token)
#
#         self.assertEqual(resp.status_code, 200)
#
#     def test_enable_remote_socket(self):
#         resp = self.client.post("/api/devices/remote-socket/1/enable/", {},
#                                 HTTP_AUTHORIZATION='Bearer ' + self.access_token)
#
#         self.assertEqual(resp.status_code, 200)
#
#     def test_disable_remote_socket(self):
#         resp = self.client.post("/api/devices/remote-socket/1/disable/", {},
#                                 HTTP_AUTHORIZATION='Bearer ' + self.access_token)
#
#         self.assertEqual(resp.status_code, 200)
