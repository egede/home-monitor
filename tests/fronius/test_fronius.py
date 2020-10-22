import unittest
from unittest import mock
import fronius


def mocked_requests_get(*args, **kwargs):
    """This method will be used by the mock to replace requests.get"""
    class MockResponse:
        def __init__(self, json_data, status_code, exception):
            self.json_data = json_data
            self.status_code = status_code
            self.exception = exception

        def json(self):
            return self.json_data

        def raise_for_status(self):
            if self.exception:
                raise self.exception
            return

    if args[0] == 'http://good_domain/solar_api/GetAPIVersion.cgi':
        return MockResponse({
            "APIVersion": 1,
            "BaseURL": "/solar_api/v1/",
            "CompatibilityRange": "1.5-16"
        }, 200, None)
    elif args[0] == 'http://version2/solar_api/GetAPIVersion.cgi':
        return MockResponse({
            "APIVersion": 2,
            "BaseURL": "/solar_api/v1/",
            "CompatibilityRange": "2.0-2.10"
        }, 200, None)
    elif args[0] == 'http://good_domain/solar_api/v1/GetInverterRealtimeData.cgi':
        print('A')
        return MockResponse({
            'Body': {'Data': {'PAC': {'Values': {'1': 1234}}}}
        }, 200, None)

    print(args[0])
    return MockResponse(None, 404, ConnectionError)


class FroniusTestCase(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_inverter(self, mock_get):
        fronius.inverter('http://good_domain')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_wrong_api(self, mock_get):
        try:
            fronius.inverter('http://version2')
        except ConnectionError as err:
            print(err)
        with self.assertRaises(ConnectionError):
            fronius.inverter('http://version2')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_wrong_server(self, mock_get):
        with self.assertRaises(ConnectionError):
            fronius.inverter('http://nowhere')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_power_getter(self, mock_get):
        i = fronius.inverter('http://good_domain')
        assert(i.power == 1234)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_power_setter(self, mock_get):
        i = fronius.inverter('http://good_domain')
        with self.assertRaises(AttributeError):
            i.power = 1000


if __name__ == '__main__':
    unittest.main()
