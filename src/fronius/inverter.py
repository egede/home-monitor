import requests
from framework.widget import widget


class inverter(widget):
    """Communicate with the Fronius inverter RESTful API and create plots."""

    def __init__(self, geometry, updateinterval, server='http://froniusinverter'):
        super().__init__(geometry, updateinterval)
        reply = self._version(server)
        if reply['APIVersion'] != 1:
            print('No support for Fronius API version different from 1')
            raise ConnectionError
        self._url = server + reply['BaseURL']

    def _version(self, server):
        r = requests.get(server + '/solar_api/GetAPIVersion.cgi')
        r.raise_for_status()
        return r.json()

    def _get(self, script, payload):
        r = requests.get(self._url + script, params=payload)
        r.raise_for_status()
        return r.json()

    @property
    def power(self):
        reply = self._get('GetInverterRealtimeData.cgi', {'Scope': 'System'})
        return reply['Body']['Data']['PAC']['Values']['1']

    def display(self, server):
        print(f'The current power is {self.power} W')
