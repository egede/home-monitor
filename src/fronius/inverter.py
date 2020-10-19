import requests


class inverter():
    """Communicate with the Fronius inverter RESTful API and create plots."""

    def __init__(self, server='http://fronius'):
        self._url = server + '/solar_api/'

    def APIversion(self):
        r = requests.get(self._url + '/GetAPIVersion.cgi')
        print(r.json())
