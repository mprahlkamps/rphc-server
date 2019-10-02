import json

import requests

from devices.controller.socket.remote_socket_controller import RemoteSocketController


class SonoffRemoteSocketController(RemoteSocketController):

    def __init__(self, ip: str, port: int, device_id: str):
        self.ip = ip
        self.port = port
        self.device_id = device_id

        self.switch_route = f'http://{self.ip}:{self.port}/zeroconf/switch'
        self.info_route = f'http://{self.ip}:{self.port}/zeroconf/info'

        self.empty_data = json.dumps({
            "deviceid": self.device_id,
            "data": {}
        })

        self.switch_on_data = json.dumps({
            "deviceid": self.device_id,
            "data": {"switch": "on"}
        })

        self.switch_off_data = json.dumps({
            "deviceid": self.device_id,
            "data": {"switch": "off"}
        })

    def enable(self):
        response = requests.post(self.switch_route, data=self.switch_on_data)

    def disable(self):
        response = requests.post(self.switch_route, data=self.switch_off_data)

    def status(self):
        response = requests.post(self.info_route, data=self.empty_data)
        json_response = json.loads(response.text)
        data = json.loads(json_response['data'])

        return data['switch']
